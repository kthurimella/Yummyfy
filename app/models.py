import datetime

from app import db


class User(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    email = db.StringField(max_length=255, required=True)
    password = db.StringField(max_length=255, required=True)