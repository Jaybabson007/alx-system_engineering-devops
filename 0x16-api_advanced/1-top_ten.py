#!/usr/bin/python3
"""This python Module consumes the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """This function queries the Reddit API and prints the titles of the first 10 hot
    posts listed for a given subreddit.

    If its not a valid subreddit, it prints None.
    Invalid subreddits may return a redirect to search results.

    Args:
        subreddit (str): subreddit

    Returns:
        str: Returns titles of the first 10 hot posts
    """
    base_url = 'https://www.reddit.com'
    sort = 'top'
    limit = 10
    url = '{}/r/{}/.json?sort={}&limit={}'.format(
        base_url, subreddit, sort, limit)
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
        Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'
    }
    response = requests.get(
        url,
        headers=headers,
        allow_redirects=False
    )
    if response.status_code == 200:
        for post in response.json()['data']['children'][0:10]:
            print(post['data']['title'])
    else:
        print(None)
