from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from flask import request as request_handler

import pymongo
from pymongo import Connection

import urllib

#from config import SECRET_KEY

SECRET_KEY = "key"

################################################################################

# defaults to /static and /templates
app = Flask(__name__)
app.secret_key = SECRET_KEY

# API ids

#Foursquare
FS_CLIENT_ID = "IGHYIIQIRRVUGIMJ05XGMGXIGH25WVZ5CLFM53C5BXXQXHTN"
FS_CLIENT_SECRET = "E4EATPZBLVLMTJSIUZRK3T2O3UGR4IARF50UP35Q0Y0KJ5TP"
FS_REDIRECT_URI = urllib.urlencode([("redirect_uri","http://ninjapiraterockstardeveloper.com/apifeedback/foursquare")])



@app.route('/')
def index():
    if not('user' in session):
        # push random user id if you don't have it
        session['user'] = "rand"
    return render_template('index.html')

@app.route('/test_api')
def test_api():
    if not('user' in session):
        pass
    return render_template('test_api.json')

@app.route('/apifeedback/foursquare')
def process_facebook():
    usercode = request_handler.args.get('code')

    request_url = "https://foursquare.com/oauth2/access_token?client_id=%s&client_secret=%s&grant_type=authorization_code&redirect_uri=%s&code=CODE", FS_CLIENT_ID, FS_CLIENT_SECRET, FS_REDIRECT_URI
    return ""

if __name__=="__main__":
    app.run(debug=True)
