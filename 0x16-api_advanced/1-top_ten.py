#!/usr/bin/python3
"""Queries the Reddit API and prints the
titles of the first 10
hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed"""
    url = r"https://www.reddit.com/r/{}/hot/.json"
    headers = {
        'User-agent': 'Mozilla/5.0',
        'Host': 'www.reddit.com',
        'Upgrade-Insecure-Requests': '0',
        'allow_redirects': '0'
    }
    response = requests.get(url.format(subreddit), headers=headers)
    if response.status_code != 200:
        print(None)
        return
    my_list = response.json().get('data').get('children')
    for x in my_list[:10]:
        data = x['data']
        title = data.get('title')
        print(title)
