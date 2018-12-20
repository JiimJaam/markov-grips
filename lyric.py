#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import numpy as np
import tweepy
import sys
import time

words = open(r'C:\Users\crucha\Downloads\DeathGrips.txt', encoding='utf8').read()

corpus = words.split()

def make_pairs(corpus):
    for i in range(len(corpus)-1):
        yield (corpus[i], corpus[i+1])
        
pairs = make_pairs(corpus)

word_dict = {}

for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]
 
first_word = np.random.choice(corpus)

chain = [first_word]

n_words = 30

for i in range(n_words):
    chain.append(np.random.choice(word_dict[chain[-1]]))

fin = str(' '.join(chain))

#enter the corresponding information from your Twitter application:
from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = environ['CONSUMER_SECRET']#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = environ['ACCESS_KEY']#keep the quotes, replace this with your access token
ACCESS_SECRET = environ['ACCESS_SECRET']#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

INTERVAL = 30 * 60 #30 minutes

api.update_status(fin)
time.sleep(INTERVAL)