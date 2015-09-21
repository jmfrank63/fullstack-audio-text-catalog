'''
Main project flask file for the audio text catalog
'''
from flask import Flask

app = Flask(__name__)

import atcatalog.views.pub_lang
import atcatalog.views.pub_text
import atcatalog.views.user_lang
import atcatalog.views.user_text
import atcatalog.views.users
