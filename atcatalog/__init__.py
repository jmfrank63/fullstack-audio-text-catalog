'''
Main project flask file for the audio text catalog
'''
from flask import Flask

app = Flask(__name__)

import atcatalog.views.publang
import atcatalog.views.userlang
import atcatalog.views.pubtext
import atcatalog.views.usertext
import atcatalog.views.users
