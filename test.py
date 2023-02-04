# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 17:43:24 2023

@author: aamir
"""

import tweepy






auth = tweepy.OAuth1UserHandler(
   "API / Consumer Key here", "API / Consumer Secret here",
   "Access Token here", "Access Token Secret here"
)
api = tweepy.API(auth)