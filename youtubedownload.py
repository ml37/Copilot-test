from pytube import YouTube

url=input("Enter the url: ")
stream = YouTube(url).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
stream.download()
print("Downloaded")