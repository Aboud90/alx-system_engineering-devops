#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of total subscribers for a given
subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    url = 'https://api.reddit.com/r/{subreddit}'
    headers = {
        'User-Agent': 'My User Agent 1.0'
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
