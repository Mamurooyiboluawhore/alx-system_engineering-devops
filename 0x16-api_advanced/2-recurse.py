#!/usr/bin/python3
""" a function that queries the Reddi API and
    prints the titles of the first 10 hot post
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mamuro'}
    params = {"after": "after"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        response = response.json()
        after = response.get("after")
        hotPost = response.get('data').get('children')
        for post in hotPost:
            hot_list.append(post.get('data').get('title'))

            if after:
                return recurse(subreddit, hot_list, after)
        return hot_list
    return None
