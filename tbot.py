# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 21:41:34 2023

@author: aamir
"""
from dotenv import load_dotenv
load_dotenv()
import json
import random
import time
import sys
import tweepy
from os import environ
"""
consumer_key1 = 'o6bF5T5It9WtHjGTVbR1zmbB1'
consumer_secret_key1 = 'uDEcRuOemqjQwaiB5pHy0aobtJNjiCq6ztHLDhpY1i54Pzv1AA'
access_token = '871329457595744256-Tb9ijBkXGIaqsDNcXZorqxGv9ID8mkU'
access_token_secret = 'HNg93RFiC2g5b50gux5aeZpTJltEv8c37T6K4CfKfmzWR'
"""
def get_quotes():
    with open('data.json') as f:
        quotes_json = json.load(f)
    return quotes_json['quotes']

def get_random_quote():
    quotes = get_quotes()
    random_quote = random.choice(quotes)
    return random_quote

def create_tweet1():
    quote = get_random_quote()
    tweet = """
            {}
            ~{}
            """.format(quote['quote'], quote['character'])
    return tweet

def tweet_quote():

   client = tweepy.Client(consumer_key='o6bF5T5It9WtHjGTVbR1zmbB1',
                         consumer_secret='uDEcRuOemqjQwaiB5pHy0aobtJNjiCq6ztHLDhpY1i54Pzv1AA',
                         access_token='871329457595744256-Tb9ijBkXGIaqsDNcXZorqxGv9ID8mkU',
                         access_token_secret='HNg93RFiC2g5b50gux5aeZpTJltEv8c37T6K4CfKfmzWR')
 
   print('getting a random quote...')
   tweet = create_tweet1()
   client.create_tweet(tweet)
         

if __name__ == "__main__":
    tweet_quote()