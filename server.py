from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from flask import request as request_handler

import pymongo
from pymongo import Connection

import requests
import json

import urllib

import pymongo
from pymongo import Connection

import hashlib

#API Imports
import etsy_api
from etsy_api import (Etsy_API, Listings)

import doco_api

from config import SECRET_KEY, PORT

# SECRET_KEY = "

################################################################################

# defaults to /static and /templates
app = Flask(__name__)
app.secret_key = SECRET_KEY

# API ids

#Foursquare
FS_CLIENT_ID = "IGHYIIQIRRVUGIMJ05XGMGXIGH25WVZ5CLFM53C5BXXQXHTN"
FS_CLIENT_SECRET = "E4EATPZBLVLMTJSIUZRK3T2O3UGR4IARF50UP35Q0Y0KJ5TP"
FS_REDIRECT_URI = urllib.urlencode([("redirect_uri","http://nyancat.ninjapiraterockstardeveloper.com/apifeedback/foursquare")])


connection = Connection()
db = connection["hacknycat"]

@app.route('/')
def index():
    if not('user' in session):
        # create a user, get the id
        post = {"points": 0}
        id = db.users.insert(post)
        session['user'] = id

    if not('lat' in session):
        session['lat'] = 40.728429

    if not('long' in session):
        session['long'] = -73.995605

    return render_template('index.html', FS_REDIRECT_URI=FS_REDIRECT_URI,
                           id= session['user'])

@app.route('/test_api')
def test_api():
    if not('user' in session):
        redirect("/")
    user = db.users.find_one({"_id":session["user"]})
    # do something with a user
    return render_template('test_api.json')

@app.route('/apifeedback/foursquare')
def process_facebook():
    usercode = request_handler.args.get('code')

    request_url = "https://foursquare.com/oauth2/access_token?\
client_id=%s&client_secret=%s&grant_type=authorization_code&%s&\
code=%s" % (FS_CLIENT_ID, FS_CLIENT_SECRET, FS_REDIRECT_URI, usercode)
    usercode_json = requests.get(request_url)
    usercode_json = json.loads(usercode_json.text)

    foursquare_url = 'https://api.foursquare.com/v2/venues/search?\
radius=1000&v=20120425&ll=%f,%f&oauth_token=\
%s' % (session['lat'],session['long'], usercode_json['access_token'])
    data = requests.get(foursquare_url)

    data = data.text
    data_json = json.loads(data)
    response = ""
    for item in data_json['response']['venues']:
        response += item['name'] + '\n'
    return response

@app.route('/google/places/')
def process_google_maps():
    """ Proxy for google places api """
    
    location    = request_handler.args.get('location')
    lat, longit = location.split(',')
    session['lat'] = float(lat)
    session['long'] = float(longit) 


    radius      = request_handler.args.get('radius')
    key         = request_handler.args.get('key')
    sensor      = request_handler.args.get('sensor')
    types       = request_handler.args.get('types')

    args = urllib.urlencode([("location", location),
                             ('radius', radius),
                             ('key', key),
                             ('sensor', sensor),
                             ('types', types)])

    google_url = "https://maps.googleapis.com/maps/api/place/search/json?"+args
    google_json = requests.get(google_url)
    google_json = google_json.text

    return google_json

@app.route('/etsy-results/')
def etsy():
    results = etsy_api.Listings().findAllListingActive('nyancat')
    data = ""
    for item in results['results']:
        data += item['title']+'<br />'
        data += item['url']+'<br />'

    return data

@app.route('/dc-results/')
def donors_choose():
    titles, links = doco_api.Geo().ProjectsNearLatLong(session['lat'],session['long'])
    return_value = ""
    idx = 0
    while idx != len(titles):
        return_value += titles[idx] + "<br />" + links[idx] + "<br />"
        idx += 1
    return return_value

@app.route('/newswire/')
def nyt():
    try:
        news_obj = db.news.find().sort("time", direction=-1)[0]
    except:
        return "Nyan "*50
    if news_obj:
        return news_obj["news"]
    else:
        return "Nyan "*50

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=PORT)
