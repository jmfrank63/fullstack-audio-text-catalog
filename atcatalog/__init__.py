# -*- coding: utf-8 -*-
'''
Main project flask file for the audio text catalog
'''
from flask import Flask

app = Flask(__name__)

import atcatalog.views.languages
import atcatalog.views.language
import atcatalog.views.sentence
