'''
The run file, a flask boiler plate.
'''
from atcatalog import app
from werkzeug.contrib.fixers import ProxyFix
from os import getenv

if __name__ == '__main__':
    app.secret_key = 'udacity_secret_app_development_key'
    app.debug = True
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(host=getenv('IP', '0.0.0.0'), port=int(getenv('PORT', '8080')))
