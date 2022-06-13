from pytube import YouTube

url=input("Enter the url: ")
"""download youtube video with inputted url"""
def download():
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    stream.download()
    print("Downloaded")

download()