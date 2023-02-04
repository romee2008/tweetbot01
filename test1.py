# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 19:00:29 2023

@author: aamir
"""

import json
import random


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
       
    print('getting a random quote...')
    tweet = create_tweet1()
    print(tweet)
   

if __name__ == "__main__":
    tweet_quote()



