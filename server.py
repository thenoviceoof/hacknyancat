from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template

# defaults to /static and /templates
app = Flask(__name__)

@app.route('/')
def index():
    # if 'id' in session:
    #     pass
    return render_template('index.html')

if __name__=="__main__":
    app.run()
