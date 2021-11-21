from unittest import TestCase
from unittest.mock import patch, MagicMock

import requests

import settings
from .api import get_tweets_by_username, get_tweets_by_hashtag, _request


class TestApi(TestCase):
    def test_get_tweets_by_username(self):
        with patch("twitter_sdk.api._request") as _request_mock:
            _request_mock.return_value = {"some": "return value"}
            return_value = get_tweets_by_username("konstunn")
            assert return_value == _request_mock.return_value
            assert _request_mock.call_count == 1
            args, kwargs = _request_mock.call_args
            assert args == ("get", "/2/tweets/search/recent"), args
            assert kwargs == {"query": "from:konstunn"}, kwargs

    def test_get_tweets_by_hashtag(self):
        with patch("twitter_sdk.api._request") as _request_mock:
            _request_mock.return_value = {"some": "return value"}
            return_value = get_tweets_by_hashtag("Python")
            assert return_value == _request_mock.return_value
            args, kwargs = _request_mock.call_args
            assert args == ("get", "/2/tweets/search/recent"), args
            assert kwargs == {"query": "#Python"}, kwargs

    @patch("twitter_sdk.api.requests.request")
    @patch("settings.TIMEOUT", 123)
    @patch("settings.TWITTER_BEARER_TOKEN", "some_twitter_bearer_token")
    def test_request(self, request_mock):
        response = request_mock.return_value = MagicMock(status_code=200)
        response.json.return_value = {"some": "json"}
        return_value = _request("get", "some/endpoint", some="kwargs")
        assert return_value == {"some": "json"}
        assert request_mock.call_count == 1
        args, kwargs = request_mock.call_args
        assert args == ("get", "https://api.twitter.com/some/endpoint"), args
        assert kwargs == {
            "params": {"some": "kwargs"},
            "timeout": settings.TIMEOUT,
            "headers": {"Authorization": "Bearer some_twitter_bearer_token"}
        }, kwargs
