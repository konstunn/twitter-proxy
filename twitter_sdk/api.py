import logging
import os
from typing import Any, Dict
from urllib.parse import urljoin

import requests

import settings


log = logging.getLogger(__file__)


class TwitterException(Exception):
    def __init__(self, *args, response=None):
        super().__init__(*args)
        self.response: requests.Response = response


def get_tweets_by_username(username: str) -> Dict[str, Any]:
    return _request("get", "/2/tweets/search/recent", query=f"from:{username}")


def get_tweets_by_hashtag(hashtag: str) -> Dict[str, Any]:
    return _request("get", "/2/tweets/search/recent", query=f"#{hashtag}")


def _request(method, endpoint, **kwargs) -> Dict[str, Any]:
    try:
        headers = {"Authorization": f"Bearer {settings.TWITTER_BEARER_TOKEN}"}
        url = urljoin("https://api.twitter.com/", endpoint)
        response = requests.request(
            method, url, params=kwargs, timeout=settings.TIMEOUT, headers=headers
        )
        response.raise_for_status()
    except requests.RequestException as exc:
        raise TwitterException(response=exc.response) from exc
    return response.json()
