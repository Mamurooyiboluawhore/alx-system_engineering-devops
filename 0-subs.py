#!/usr/bin/python3
""" a function that queries"""
import requests


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User_Agent': 'This User'}
    response = requests.get(url, headers=headers, allow_redirects=False).json()
    if response.status_code   == 200:
        data = response.get('data').get('subscribers')
        return data
    else:
        return(0)
    
