from pytube import YouTube
from pytube import Channel
import ffmpeg
import tkinter
import os

root = tkinter.Tk()

def AudioClick():
    lbl2.config(text="Audio Downloading...")
    print("Audio Download Button Clicked") 
    urlInput = txt.get()
    print(urlInput)
    yt = YouTube(urlInput)
    stream = yt.streams.filter(only_audio=True).get_audio_only()
    stream.download()
    lbl2.config(text="Downloaded")
    print("Download Complete")

def chClick():
    print('Channel Download Button Clicked')
    channelInput = txt.get()
    print('----')
    print(channelInput)
    ch = Channel(channelInput)
    print('----')
    print('walalalalalalaru')
    print(ch)
    print('----')
    """download all video in channel"""
    print(f'Downloading videos by: {ch.channel_name}')
    for video in ch.videos:
        print(video)
        print('-------')
        video.streams.filter(progressive=True).order_by('resolution').desc().first().download()

def VideoClick():
    lbl2.config(text="Video Downloading...")
    print("Video Download Button Clicked")
    urlInput = txt.get()
    print(urlInput)
    yt = YouTube(urlInput)
    stream = yt.streams.filter(progressive=True).order_by('resolution').desc().first()
    stream.download()
    lbl2.config(text="Downloaded")
    print("Download Complete")

    

root.title("Youtube Audio Downloader")
root.configure(background='#f2f2f2')
lbl = tkinter.Label(root, text="URL", font=("Arial Bold", 20))
lbl.grid(column=0, row=0)
txt = tkinter.Entry(root, width=50, font=("Arial Bold", 20))
txt.grid(column=1, row=0)
btn = tkinter.Button(root, text="Audio", font=("Arial Bold", 20), command=AudioClick)
btn.grid(column=2, row=0)
btn2 = tkinter.Button(root, text="Video", font=("Arial Bold", 20), command=VideoClick)
btn2.grid(column=3, row=0)
btn3 = tkinter.Button(root, text='Channel', font=("Arial Bold", 20), command=chClick)
btn3.grid(column=4, row=0)
lbl2 = tkinter.Label(root, text="Ready", font=("Arial Bold", 20))
lbl2.grid(column=0, row=1)

root.mainloop()