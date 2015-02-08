import os
basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
MONGODB_SETTINGS = {'DB': 'heroku_app33806434',
                    'host': 'mongodb://heroku_app33806434:st581cog5a31e5n2s2bg0i173u@ds041651.mongolab.com:41651/heroku_app33806434'
}
