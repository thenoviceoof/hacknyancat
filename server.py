from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template

import pymongo

# defaults to /static and /templates
app = Flask(__name__)
app.secret_key="eaf42496e70cdd2f73ea9a9fe56c19c3"

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

if __name__=="__main__":
    app.run(debug=True)
