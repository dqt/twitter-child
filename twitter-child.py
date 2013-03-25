'''
twitter-child is an AI bot for twitter. it uses tweepy to interact with the
twitter API and gets its intelligence from cleverbot. it was written by
dqt and you are free to do as you please with it.

author: dqt
twitter.com/dqt
digitalgangster.com
'''


import requests
import tweepy
import logging
import sys


# Make a global logging object.
x = logging.getLogger("log")
x.setLevel(logging.DEBUG)

# This handler writes everything to a file.
h1 = logging.FileHandler("twitter-child.log")
f = logging.Formatter("%(levelname)s %(asctime)s %(funcName)s %(lineno)d %(message)s")
h1.setFormatter(f)
h1.setLevel(logging.DEBUG)
x.addHandler(h1)

# This handler emails me anything that is an error or worse.
h2 = logging.StreamHandler()
h2.setLevel(logging.DEBUG)
f2 = logging.Formatter("%(levelname)s: %(message)s")
h2.setFormatter(f2)
x.addHandler(h2)

username = 'decrypts'
password = ''

x.info('Using twitter username %s: ', username)
password = raw_input('Please enter password: ')
x.debug('Logging into twitter using %s:%s', username, password)

try:
    auth = tweepy.auth.BasicAuthHandler(username, password)
    x.info('Login successful using %s:%s', username, password)
except Exception, err:
    x.warning('Login failed!')
    x.debug('Login failed using %s:%s', username, password)
    x.warning('Program will exit!')
    x.exception(err)
    sys.exit(1)

api = tweepy.API(auth)

api.update_status('Updating using basic authentication via Tweepy!')

















