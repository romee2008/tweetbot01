#!/usr/bin/python
# encoding=utf8

"""
Created on Mon Jan 30 23:16:21 2023

@author: aamir
"""
from dotenv import load_dotenv
load_dotenv()
import json
import json
import random
import tweepy
import credentials
import time
import sys
from os import environ


"""
consumer_key1 = 'o6bF5T5It9WtHjGTVbR1zmbB1'
consumer_secret_key1 = 'uDEcRuOemqjQwaiB5pHy0aobtJNjiCq6ztHLDhpY1i54Pzv1AA'
access_token1 = '871329457595744256-Tb9ijBkXGIaqsDNcXZorqxGv9ID8mkU'
access_token_secret1 = 'HNg93RFiC2g5b50gux5aeZpTJltEv8c37T6K4CfKfmzWR'
"""

consumer_key1 = credentials.CONSUMER_KEY
consumer_secret_key1 = credentials.CONSUMER_SECRET_KEY
access_token1 = credentials.ACCESS_TOKEN
access_token_secret1 = credentials.ACCESS_TOKEN_SECRET


"""
consumer_key1 = environ['CONSUMER_KEY']
consumer_secret_key1 = environ['CONSUMER_SECRET_KEY']
access_token1 = environ['ACCESS_TOKEN']
access_token_secret1 = environ['ACCESS_TOKEN_SECRET']
"""

def get_quotes():
    with open('quotes1.json',encoding=('UTF-8')) as f:
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
            """.format(quote['quote'], quote['author'])
    return tweet


def tweet_quote():
    client = tweepy.Client(consumer_key=consumer_key1,
                           consumer_secret = consumer_secret_key1,
                           access_token=access_token1,
                           access_token_secret = access_token_secret1)
    
    print('getting a random quote...')
    tweet = create_tweet1()
    client.create_tweet(text=tweet)  
   

if __name__ == "__main__":
    tweet_quote()