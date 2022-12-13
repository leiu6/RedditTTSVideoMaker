from moviepy import editor
import random


def get_clip(path):
    return editor.VideoFileClip(path)


def crop_vertical_and_shorten(clip, start_t, length):
    # Grab only section of the video
    clip = clip.subclip(start_t, length + start_t)

    # Get the old dimensions of the video
    old_height = clip.size[1]
    old_width = clip.size[0]

    # Get the aspect ratio of the YouTube short
    new_aspect_ratio = old_height / old_width  # should be 9:16 for vertical 1080p

    # Get the crop dimensions
    new_height = old_height
    new_width = new_aspect_ratio * new_height
    x1 = (old_width - new_width) / 2
    x2 = x1 + new_width

    # Crop the clip
    clip = clip.crop(
        x1=x1,
        y1=0,
        x2=x2,
        y2=new_height
    )

    return clip


def get_video_length_seconds(clip):
    return clip.duration


def get_edited_clip(clip, desired_length):
    total_clip_length = get_video_length_seconds(clip)
    clip_start_time = random.randint(0, total_clip_length - desired_length)

    return crop_vertical_and_shorten(clip, clip_start_time, desired_length)


def write_video_file(clip, path):
    clip.write_videofile(path)
