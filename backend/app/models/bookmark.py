from app.extensions import db
from datetime import datetime
import string
import random


class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=True)
    url = db.Column(db.Text, nullable=False)
    short_url = db.Column(db.String(3), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    visits = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    def generate_short_characters(self):
        characters = string.digits + string.ascii_letters
        picked_chars = random.choice(characters, 3)



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.short_url = self.generate_short_characters()

    def __repr__(self):
        return f'Bookmark >>> {self.url}'
