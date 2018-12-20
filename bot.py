import tweepy
import sys
import time

from generate_lyric import fin

from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

INTERVAL = 30 * 60 #30 minutes

while True:
    lyric = get_lyric()
    api.update_status(lyric)
    time.sleep(INTERVAL)