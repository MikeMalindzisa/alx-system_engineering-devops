#!/usr/bin/python3
"""
Subredit Subcribers
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers from the Reddit API"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-agent': 'Mozilla/5.0',
        'Host': 'www.reddit.com',
        'Upgrade-Insecure-Requests': '0'
    }

    try:
        response = requests.get(url, headers=headers)
        if response.text.strip():
            data = response.json().get('data', {})
            return data.get('subscribers', 0)
        else:
            return 0
    except requests.exceptions.RequestException as e:
        return 0
