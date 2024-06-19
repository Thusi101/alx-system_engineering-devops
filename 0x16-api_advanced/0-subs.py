#!/usr/bin/python3
""" Queries the Reddit API and returns the
number of subscribers for a given subreddit. """

import requests
headers = {"User-Agent": "ubuntu:alx:v1.0 (by /u/Thusi101)"}

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    user_agent = "person_at_school"
    header = {'User-Agent': user_agent}
    resp = requests.get(url, headers=header, allow_redirects=False)
    if (resp.status_code != 200):
        return 0
    else:
        return(resp.json()['data']['subscribers'])
