# tests/test_repositories.py
from unittest import TestCase
from app.models import Tweet
from app.repositories import TweetRepository

class TestTweetRepository(TestCase):

    def test_init_return_empty_list(self):
        tweet_repository = TweetRepository()
        self.assertEqual(len(tweet_repository.tweets), 0)

    def test_add_a_tweet(self):
        tweet_repository = TweetRepository()
        tweet = Tweet("RAPH")
        tweet_repository.add(tweet)
        self.assertEqual(len(tweet_repository.tweets), 1)

    def test_auto_increment_after_adding_a_tweet(self):
        tweet_repository = TweetRepository()
        tweet = Tweet("RAPH")
        tweet2 = Tweet("JOHN")
        tweet_repository.add(tweet)
        tweet_repository.add(tweet2)
        self.assertEqual(tweet.id, 1)
        self.assertEqual(tweet2.id, 2)

    def test_get_tweet(self):
        tweet_repository = TweetRepository()
        tweet = Tweet("RAPH")
        tweet_repository.add(tweet)
        self.assertEqual(tweet, tweet_repository.get(1))
        self.assertIsNone(tweet_repository.get(2))
