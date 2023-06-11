
from pytube import YouTube

Download_folder = "/Users/sugam"


def youtube_download():
    print("https://youtu.be/2-crBg6wpp0")
    vid = input()

    # if vid[:17] == "https://youtu.be/":
    video_obj = YouTube(vid)
    stream = video_obj.streams.get_highest_resolution()
    print("Downloading...")
    if stream.download(Download_folder):
        print('Successfully downloaded')
        return
    else:
        print("You entered wrong Url must check whether it is youtube url....")


youtube_download()