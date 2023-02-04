# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 22:48:53 2023

@author: aamir
"""
import tweepy,time,sys
L = ["usa\n", "russia\n", "pakistan\n"]
  
# writing to file
file1 = open('myfile4.txt', 'w')
file1.writelines(L)
file1.close()


client = tweepy.Client(consumer_key='o6bF5T5It9WtHjGTVbR1zmbB1',
                       consumer_secret='uDEcRuOemqjQwaiB5pHy0aobtJNjiCq6ztHLDhpY1i54Pzv1AA',
                       access_token='871329457595744256-Tb9ijBkXGIaqsDNcXZorqxGv9ID8mkU',
                       access_token_secret='HNg93RFiC2g5b50gux5aeZpTJltEv8c37T6K4CfKfmzWR')



# Using readlines()
file1 = open('myfile4.txt', 'r')
Lines = file1.readlines()
  
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    response = client.create_tweet(text=line)
    time.sleep(10)
    print("Line{}: {}".format(count, line.strip()))