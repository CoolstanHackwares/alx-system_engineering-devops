#!/usr/bin/python3
'''A function that queries the Reddit API and returns the number of subscribers.
'''
import requests


BASE_URL = 'https://www.reddit.com'
'''Reddit's base API URL.
'''


def number_of_subscribers(subreddit):
    '''Retrieves the number of subscribers in a given subreddit.
    '''
    # Define custom User-Agent header to mimic a browser request
    headers = {
        'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62')
    }

    # Construct URL for the subreddit's about page
    url = f'{BASE_URL}/r/{subreddit}/about.json'

    # Send GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if request was successful (status code 200)
    if response.status_code == 200:
        # Parse JSON response and extract number of subscribers
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    else:
        # Return 0 if subreddit is invalid or not found
        return 0
