#!/usr/bin/python3
""" Queries the Reddit API and returns the
number of subscribers for a given subreddit. """

import requests
headers = {"User-Agent": "ubuntu:alx:v1.0 (by /u/Thusi101_)"}

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
