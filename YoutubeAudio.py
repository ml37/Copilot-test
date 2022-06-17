from pytube import YouTube
from pytube import Channel
import ffmpeg
import tkinter
import os

root = tkinter.Tk()

def URLClick():
    print("URL Download Button Clicked") 
    urlInput = txt.get()
    print(urlInput)
    yt = YouTube(urlInput)
    stream = yt.streams.filter(only_audio=True).get_audio_only()
    stream.download()
    lbl2 = tkinter.Label(root, text="Download Complete", font=("Arial Bold", 20))
    lbl2.grid(column=0, row=1)
    print("Download Complete")

def chClick():
    print('Channel Download Button Clicked')
    channelInput = txt.get()
    print('----')
    print(channelInput)
    ch = Channel(channelInput)
    print('----')
    print(ch)
    print('----')
    print(f'Downloading videos by: {ch.channel_name}')
    for video in ch.videos:
        video.streams.first().download()
    

root.title("Youtube Audio Downloader")
root.configure(background='#f2f2f2')
lbl = tkinter.Label(root, text="URL", font=("Arial Bold", 20))
lbl.grid(column=0, row=0)
txt = tkinter.Entry(root, width=50, font=("Arial Bold", 20))
txt.grid(column=1, row=0)
btn = tkinter.Button(root, text="Download", font=("Arial Bold", 20), command=URLClick)
btn.grid(column=2, row=0)
btn2 = tkinter.Button(root, text='Channel', font=("Arial Bold", 20), command=chClick)
btn2.grid(column=3, row=0)

root.mainloop()