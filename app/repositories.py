# app/repositories.py
# pylint: disable=missing-docstring

class TweetRepository():
    def __init__(self):
        self.clear()

    def add(self, tweet):
        self.tweets.append(tweet)
        tweet.id = self.id
        self.id += 1

    def get(self, id):
        for tweet in self.tweets:
            if id == tweet.id:
                return tweet
        return None

    def list(self):
        return [tweet for tweet in self.tweets]

    def remove(self, id):
        for tweet in self.tweets:
            if id == tweet.id:
                import pdb;pdb.set_trace()
                self.tweets.pop(id)

    def clear(self):
        self.tweets = []
        self.id = 1
