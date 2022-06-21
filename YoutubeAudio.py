from pytube import YouTube
from pytube import Channel
import tkinter
from tkinter.ttk import *

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

    
root.title("Youtube Downloader")
root.configure(background='#f2f2f2')
lbl = tkinter.Label(root, text="URL", font=("Arial Bold", 20)).grid(row=0, column=2)
txt = tkinter.Entry(root, width=50, font=("Arial Bold", 20)).grid(column=0, row=0)
btn = tkinter.Button(root, text="Audio", font=("Arial Bold", 20), background='#818D92',command=AudioClick).grid(row=1, column=1)
btn2 = tkinter.Button(root, text="Video", font=("Arial Bold", 20), background='#818D92',command=VideoClick).grid(row=1, column=2)
btn3 = tkinter.Button(root, text='Channel', font=("Arial Bold", 20), background='#818D92', command=chClick).grid(row=1, column=3)
lbl2 = tkinter.Label(root, text="Ready", font=("Arial Bold", 20)).grid(row=1, column=0)

root.mainloop()