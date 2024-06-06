#!/usr/bin/python3
"""
Subredit Subcribers
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    headers = {
        'User-agent': 'Mozilla/5.0',
        'Host': 'www.reddit.com',
        'Upgrade-Insecure-Requests': '1'
    }
    api_endpoint = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(api_endpoint, headers=headers)
    package = response.json()

    try:
        return package.get('data').get('subscribers')

    except Exception:
        return 0
