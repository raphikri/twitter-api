# app/apis/tweets.py
# pylint: disable=missing-docstring

from flask_restx import Namespace, Resource, fields
from app.db import tweet_repository

api = Namespace('tweets')

@api.route('/<int:id>')
@api.response(404, 'Tweet not found')
@api.param('id', 'Id of tweet')
class TweetResource(Resource):
    def get(self, id):
        tweet = tweet_repository.get(id)
        if tweet is None:
            api.abort(404)
        else:
            return tweet.as_dict()
