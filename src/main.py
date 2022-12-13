import scraper
import pandas as pd
from dotenv import load_dotenv

# 12 hour relaxing minecraft parkour
BACKGROUND_VIDEO: str = "https://www.youtube.com/watch?v=a5S-YhfjZdI"
DOWNLOAD_PATH: str = "../raw_video"


def main():
    reddit_instance = scraper.reddit_login()
    ask_reddit = scraper.get_subreddit(reddit_instance, "AskReddit")

    df = pd.DataFrame()

    titles = []
    scores = []
    ids = []


if __name__ == "__main__":
    main()
