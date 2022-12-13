import praw
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import os
import time

USER_AGENT = "praw_scraper_1"
BROWSER = "firefox"  # set this to chrome, edge, or safari if that is what you are using
WEBDRIVER_PATH = "../driver/geckodriver2.exe"


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


def get_reddit_screenshot(comment_url):
    # Grab the web driver
    driver = webdriver.Firefox(
        executable_path=GeckoDriverManager().install()
    )

    driver.get(comment_url)  # go to the page with the comment
    time.sleep(1)  # wait so that reddit doesn't get suspicious
