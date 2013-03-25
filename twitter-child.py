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


# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="bKKGk5LL7zwfaQrO8Oew"
consumer_secret=""

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token="928433282-5PK07buv76ah499iW2NfabrO4l5K1cpDOLtRRm6s"
access_token_secret=""


x.debug('Getting consumer secret from user')
consumer_secret = raw_input('Please enter consumer secret: ')
x.debug('Getting access token secret from user')
access_token_secret = raw_input('Please enter access token secret: ')

try:
    x.info('Attempting 0Auth login')
    x.debug('Authenticating...')
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    x.debug('Setting access token...')
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    x.info('Logged into %s', api.me().name)
except Exception, err:
    x.warning('Login failed!')
    x.warning('Program will exit!')
    x.exception(err)
    sys.exit(1)

x.info('Attempting status update')
api.update_status('Updating using OAuth authentication via Tweepy!')









