'''
twitter-child is an AI bot for twitter. it uses tweepy to interact with the
twitter API and gets its intelligence from cleverbot. it was written by
dqt and you are free to do as you please with it.

author: dqt
twitter.com/dqt
digitalgangster.com
'''


import tweepy
import logging
import sys
import time
from cleverget import Cleverget
import re

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
consumer_key="Gg1qDOHdtyuOr90V1I5iQ"
consumer_secret=""

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token="928433282-5a2iXT944KrgBaRuv60Utz02BLmLIGegZgrMTzM8"
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

#TODO Use database rather than text file
seen_ids = [line.strip() for line in open('seen_ids.txt')]


def ask_bot():
        while True:
            global seen_ids
            x.info('Getting new mentions')
            for tweet in api.mentions_timeline():
                if tweet.id not in seen_ids:
                    x.info('Found new mention!')
                    x.info('Attempting to get reply from Cleverbot')
                    q = re.sub("@decrypts ","",tweet.text,count=1)
                    x.info('Sending: %s',q)
                    cg = Cleverget(q)
                    x.info('Replying to status')
                    response = '@'+tweet.user.screen_name+' '+cg.response()
                    a = re.sub("Cleverbot","Decrypts",response,count=1)
                    api.update_status(a, tweet.id)
                    x.info('Reply successful!')
                    seen_ids.append(tweet.id)
                    doc = open('seen_ids.txt', 'a')
                    doc.write(str(tweet.id)+"\n")
                else:
                    pass
            time.sleep(70)


def main():
    ask_bot()


if __name__ == '__main__':
    main()




