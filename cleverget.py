'''
This class takes a string sends it to cleverbot and returns the response
'''

from cleverbot import Cleverbot


class Cleverget(object):
    def __init__(self, tweet):
        self.tweet = tweet

    def response(self):
        cb = Cleverbot()
        resp = cb.ask(self.tweet)
        return resp
