'''
This class takes a string sends it to cleverbot and returns the response
'''

import requests

class cleverget(object):
    def __init__(self, tweet):
        self.tweet = tweet

    def response(self):

