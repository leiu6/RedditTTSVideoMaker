import download
import editor
import scraper
import text_to_speech as tts

# 12 hour relaxing minecraft parkour
BACKGROUND_VIDEO: str = "https://www.youtube.com/watch?v=c37Lw2ZmGU8"


def main():
    # Let's generate a YouTube short
    #
    # First, we must download the background video

    yt_object = download.get_object(BACKGROUND_VIDEO)
    # download.get_video_1080(yt_object, "../raw_video/")

    title = download.get_video_title(yt_object)

    # Next, we will get a random part of the video and crop it
    clip = editor.get_clip(f"../raw_video/{title}.mp4")

    # Find a comment to use
    clist = scraper.comments_from_submission_url(
        "https://www.reddit.com/r/AskReddit/comments/zk8wn9/not_using_110_how_attractive_are_you/", 20)

    print(clist[0])

    # Create the screenshot
    scraper.get_reddit_screenshot(clist[5][1] + "?sort=top", clist[5][0], f"../screenshots/{title}.png")

    # Create the audio
    tts.talk_to_file(clist[5][0], f"../audio_clips/{title}.mp3")

    # Now edit it all together
    length = editor.get_audio_length(f"../audio_clips/{title}.mp3")
    print(length)

    # Set clip to proper length
    clip2 = editor.get_edited_clip(clip, length)

    # Superimpose image
    clip3 = editor.superimpose_image(clip2, f"../screenshots/{title}.png", length)

    # Add audio
    clip4 = editor.add_audio(clip3, f"../audio_clips/{title}.mp3")

    # Create file
    editor.write_video_file(clip4, f"../final_product/{clist[5][0]}.mp4")


if __name__ == "__main__":
    main()
