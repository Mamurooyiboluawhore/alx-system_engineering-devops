#!/usr/bin/python3

"""  function that queries"""
import requests


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Mamus'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        response = response.json()
        data = response.get('data').get('subscribers')
        return data
    return 0
