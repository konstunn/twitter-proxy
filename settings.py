import os
import logging

log = logging.getLogger(__file__)

TWITTER_BEARER_TOKEN = os.environ.get("TWITTER_BEARER_TOKEN")
TIMEOUT = 10

if TWITTER_BEARER_TOKEN is None:
    log.warning("TWITTER_BEARER_TOKEN is None")
