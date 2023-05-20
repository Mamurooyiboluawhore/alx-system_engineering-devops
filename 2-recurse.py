#!/usr/bin/python3
""" a function that queries the Reddi API and
    prints the titles of the first 10 hot post
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mamuro'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        response = response.json().get('data').get('children')
        for post in response:
            hot_list.append(post.get('data').get('title'))
        after = response.get("data").get("after")

        if after:
             recurse(subreddit, hot_list, after)
        return hot_list
    return None
