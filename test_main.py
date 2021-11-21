from unittest import TestCase
from unittest.mock import patch

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


class TestMain(TestCase):
    def test_get_tweets_by_username(self):
        with patch("twitter_sdk.get_tweets_by_username") as get_tweets_by_username_mock:
            get_tweets_by_username_mock.return_value = {"some_response": "from twitter"}
            response = client.get("/users/konstunn")
            assert response.status_code == 200
            assert response.json() == get_tweets_by_username_mock.return_value
            assert get_tweets_by_username_mock.call_count == 1
            args, kwargs = get_tweets_by_username_mock.call_args
            assert args == ("konstunn",)
            assert kwargs == {}

    def test_get_tweets_by_hashtag(self):
        with patch(
            "main.twitter_sdk.get_tweets_by_hashtag"
        ) as get_tweets_by_hashtag_mock:
            get_tweets_by_hashtag_mock.return_value = {"some_response": "from twitter"}
            response = client.get("/hashtags/Python")
            assert response.status_code == 200
            assert response.json() == get_tweets_by_hashtag_mock.return_value
            assert get_tweets_by_hashtag_mock.call_count == 1
            args, kwargs = get_tweets_by_hashtag_mock.call_args
            assert args == ("Python",)
            assert kwargs == {}
