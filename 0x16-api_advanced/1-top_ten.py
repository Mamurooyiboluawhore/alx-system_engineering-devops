#!/usr/bin/python3
""" a function that queries the Reddi API and
    prints the titles of the first 10 hot post
"""
import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mamuro'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        response = response.json()
        hotPost = response.get('data').get('children')
        for post in hotPost:
            print(post.get('data').get('title'))
    else:
        print(None)
