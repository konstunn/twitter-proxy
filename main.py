from typing import Dict, Any

from fastapi import FastAPI
import twitter_sdk

app = FastAPI()


@app.get("/hashtags/{hashtag}")
async def get_tweets_by_hashtag(hashtag: str) -> Dict[str, Any]:
    return twitter_sdk.get_tweets_by_hashtag(hashtag)


@app.get("/users/{username}")
async def get_tweets_by_user(username: str) -> Dict[str, Any]:
    return twitter_sdk.get_tweets_by_username(username)
