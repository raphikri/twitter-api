# app/apis/tweets.py
# pylint: disable=missing-docstring

from flask_restx import Namespace, Resource, fields, reqparse
from flask import request
from app.db import tweet_repository
from app.models import Tweet


api = Namespace('tweets')

post_parser = api.model('New tweet', {
    'text': fields.String(required=True)
})

tweet = api.model('Tweet', {
    'id': fields.Integer,
    'text': fields.String,
    'created_at': fields.DateTime
})

@api.route('/<int:id>')
@api.response(404, 'Tweet not found')
@api.param('id', 'Id of tweet')
class TweetResource(Resource):
    @api.doc('GET a tweet')
    @api.marshal_with(tweet)
    def get(self, id):
        tweet = tweet_repository.get(id)
        if tweet is None:
            api.abort(404, f"Tweet {id} doesn't exist")
        else:
            return tweet # tweet.as_dict()

    def delete(self, id):
        tweet = tweet_repository.get(id)
        if tweet is not None:
            tweet_repository.remove(id)
        return '', 204

    @api.marshal_with(tweet, code=204)
    @api.expect(post_parser)
    def patch(self, id):
        tweet = tweet_repository.get(id)
        if tweet is None:
            api.abort(404, f"Tweet {id} doesn't exist")
        else:
            tweet.text = api.payload["text"]
            return tweet, 204

@api.route('/')
@api.response(422, 'Invalid tweet')
class TweetResource(Resource):
    @api.doc('POST a tweet')
    @api.marshal_with(tweet, code=201)
    @api.expect(post_parser)
    def post(self):
        text = api.payload["text"]
        tweet = Tweet(text)
        tweet_repository.add(tweet)
        return tweet, 201

    @api.doc('List a tweet')
    @api.marshal_with(tweet)
    def get(self):
        tweet = tweet_repository.list()
        return tweet
