# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 20:01:05 2023

@author: aamir
"""
import requests 
def get_quote():
    URL = "https://api.quotable.io/random"
    try:
        response = requests.get(URL)
    except:
        print("Error while calling API...")
        
        
        