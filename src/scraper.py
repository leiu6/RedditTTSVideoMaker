import praw
from dotenv import load_dotenv
import os

USER_AGENT = "praw_scraper_1"


def reddit_login():
    load_dotenv(
        dotenv_path="../.env"
    )

    return praw.Reddit(
        username=os.getenv("REDDIT_USERNAME"),
        password=os.getenv("REDDIT_PASSWORD"),
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        user_agent=USER_AGENT
    )


def get_subreddit(reddit_instance, subreddit_name):
    return reddit_instance.subreddit(subreddit_name)


def get_top_submissions(subreddit_name, amount):
    subreddit_obj = get_subreddit()
