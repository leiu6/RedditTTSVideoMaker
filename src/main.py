import scraper

# 12 hour relaxing minecraft parkour
BACKGROUND_VIDEO: str = "https://www.youtube.com/watch?v=a5S-YhfjZdI"
DOWNLOAD_PATH: str = "../raw_video"


def main():
    scraper.get_reddit_screenshot()


if __name__ == "__main__":
    main()
