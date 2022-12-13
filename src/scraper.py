import praw
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
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


def comments_from_submission_url(url, number):
    reddit = reddit_login()  # login to reddit

    # Get the submission
    submission = reddit.submission(url=url)
    submission.comment_sort = "top"
    submission.comments.replace_more(limit=0)

    comment_list = list(submission.comments)

    output = list()

    counter = 0
    for comment in comment_list:
        if counter < number:
            output.append((comment.body, comment.submission.url))
            counter += 1
        else:
            continue

    return output


def get_reddit_screenshot(comment_url, search_string, path):
    # Grab the web driver
    driver = webdriver.Firefox(
        executable_path=GeckoDriverManager().install()
    )

    driver.get(comment_url)  # go to the page with the comment
    time.sleep(1)  # wait so that reddit doesn't get suspicious

    comment_xpath = f"//p[contains(string(), \"{search_string}\")]/parent::div/parent::div/parent::div/parent::div" \
                    f"/parent::div/parent::div/parent::div/parent::div "

    element = driver.find_element(By.XPATH, comment_xpath)

    element.screenshot(path)

    driver.close()
