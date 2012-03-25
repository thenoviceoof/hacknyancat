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
        session['user'] = id["_id"]
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

    request_url = "https://foursquare.com/oauth2/access_token?client_id=%s&client_secret=%s&grant_type=authorization_code&%s&code=%s" % (FS_CLIENT_ID, FS_CLIENT_SECRET, FS_REDIRECT_URI, usercode)
    usercode_json = requests.get(request_url)
    usercode_json = json.loads(usercode_json.text)

    return "Hello World \n" + str(usercode_json['access_token'] )

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=PORT)
