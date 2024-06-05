#!/usr/bin/python3
'''A function that queries the Reddit API and returns the number of subscribers'''

import requests

BASE_URL = 'https://www.reddit.com'
'''Reddit's base API URL'''


def number_of_subscribers(subreddit):
    '''Retrieves the number of subscribers in a given subreddit.
    '''
    # Define custom User-Agent header to mimic a browser request
    user_agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) '
                      'Gecko/20100101 Firefox/126.0'
    }
    url = f'{BASE_URL}/r/{subreddit}/about.json'

    # Send GET request to the Reddit API
    response = requests.get(url, headers=user_agent, allow_redirects=False)

    # Check if request was successful (status code 200)
    if response.status_code == 200:
        # Parse JSON response and extract number of subscribers
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    else:
        # Return 0 if subreddit is invalid or not found
        return 0
