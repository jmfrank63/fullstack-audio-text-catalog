'''
Main project flask file for the audio text catalog
'''
from flask import Flask

app = Flask(__name__)

import atcatalog.views.publangs
import atcatalog.views.pubsents
import atcatalog.views.userlang
import atcatalog.views.usersents
import atcatalog.views.userauth
