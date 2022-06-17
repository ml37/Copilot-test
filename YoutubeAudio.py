from pytube import YouTube

url=input("Enter the url: ")
yt = YouTube(url)
stream = yt.streams.filter(adaptive=True).order_by('resolution').desc().first()
stream.download()