from pytube import YouTube
print("Video will be downloaded in the present directory.")
print("Please enter the link of the youtube video:")
video_link = input()
try:
    yt = YouTube(video_link)
except VideoUnavailable:
    print(f"The video is unaccessible to you. Try again with another url.")
else:
    print(f"Title of the video: {yt.title}.")
    print("Your video is downloading...")
    stream = yt.streams.get_by_itag(22)
    stream.download()
    print("Download complete.")
    print("Enjoy.")