'''
Main project flask file for the audio text catalog
'''
from flask import Flask

app = Flask(__name__)

import atcatalog.languages
import atcatalog.users
