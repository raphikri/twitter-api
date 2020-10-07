# app/models.py
# pylint: disable=missing-docstring
import datetime


class Tweet():
    def __init__(self, text):
        self.id = None
        self.text = text
        self.created_at = datetime.datetime.now()

    def as_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'created_at': str(self.created_at)
        }
