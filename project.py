'''
Main project flask file for the audio text catalog
'''
from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

from os import getenv

app = Flask(__name__)

@app.route('/')
def show_root():
    return "Hello Audio Text Catalog!"

if __name__ == '__main__':
    app.secret_key = 'udacity_secret_app_development_key'
    app.debug = True
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(host=getenv('IP','0.0.0.0'), port=int(getenv('PORT', '8080')))
