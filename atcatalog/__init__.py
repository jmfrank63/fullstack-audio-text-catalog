# -*- coding: utf-8 -*-
'''
Main project flask file for the audio text catalog
'''
from flask import Flask
from flask_login import LoginManager
from flask.ext.breadcrumbs import Breadcrumbs, register_breadcrumb
from os import getenv


app = Flask(__name__)

app.secret_key = getenv('FLASK_SECRET', 'udacity_super_secret_key')
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/login"
Breadcrumbs(app=app)


import atcatalog.views.home
import atcatalog.views.users
import atcatalog.views.languages
import atcatalog.views.language
import atcatalog.views.sentence
