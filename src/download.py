from pytube import YouTube


ITAG_RESOLUTION_1080 = 137
ITAG_RESOLUTION_720 = 136


def get_object(url):
    return YouTube(url)


def get_video_title(obj):
    return obj.title


def get_video_1080(obj, path):
    # Grab stream object
    stream = obj.streams.filter(
        adaptive=True,
        file_extension='mp4'
    ).get_by_itag(ITAG_RESOLUTION_1080)

    # If the stream does not exist then we return False
    if stream is None:
        return False

    # Download the file
    stream.download(path)
    return True


def get_video_720(obj, path):
    stream = obj.streams.filter(
        adaptive=True,
        file_extension='mp4'
    ).get_by_itag(ITAG_RESOLUTION_720)

    if stream is None:
        return False

    stream.download(path)
    return True
