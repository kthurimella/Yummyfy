import os
basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
MONGODB_SETTINGS = {'DB': 'heroku_app33806434',
                    'host': 'mongodb://heroku_app33806434@ds041821.mongolab.com:41821/heroku_app33806434'
}
