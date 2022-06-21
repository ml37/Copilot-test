from pytube import YouTube
from pytube import Channel
import tkinter
import os
from os import path
import shutil
from re import T
from tkinter import *
from tkinter import ttk

cd =os.getcwd()
root = tkinter.Tk()
print(f'start position {cd}')
if os.path.isdir('Audio') == True :
    print('Audio Folder Already Exists')
else:
    os.mkdir('Audio')
if os.path.isdir('Video') == True :
    print('Video Folder Already Exists')
else:
    os.mkdir('Video')
if os.path.isdir('channel') == True :
    print('channel Folder Already Exists')
else:
    os.mkdir('channel')

def AudioClick():
    print("Audio Download Button Clicked") 
    urlInput = txt.get()
    print(urlInput)
    yt = YouTube(urlInput)
    stream = yt.streams.filter(only_audio=True).get_audio_only()
    stream.download()
    shutil.move(f'{yt.title}.mp4', f'Audio/{yt.title}.mp4')
    print("Download Complete")

def VideoClick():
    print("Video Download Button Clicked")
    urlInput = txt.get()
    print(urlInput)
    yt = YouTube(urlInput)
    stream = yt.streams.filter(progressive=True).order_by('resolution').desc().first()
    stream.download()
    shutil.move(f'{yt.title}.mp4', f'Video/{yt.title}.mp4')
    print("Download Complete")

def chVideoClick():
    print('Channel Download Button Clicked')
    channelInput = txt.get()
    ch = Channel(channelInput)
    print(f'Downloading videos by: {ch.channel_name}')
    print('Channel Video List')
    print(ch)
    if os.path.isdir(f'channel/{ch.channel_name}') == True :
        print(f'Channel {ch.channel_name} Folder Exists')
    else:
        os.mkdir(f'channel/{ch.channel_name}')
    if os.path.isdir(f'channel/{ch.channel_name}/Video') == True :
        print(f'Channel {ch.channel_name} Video Folder Exists')
    else :
        os.mkdir(f'channel/{ch.channel_name}/Video')
    print('----')
    print('Channel Video Download Start')
    os.chdir(f'channel/{ch.channel_name}/Video')
    for video in ch.videos:
        print('-------')
        print(video.title)
        if os.path.isfile(f'{video.title}.mp4') == False :
            print(f'Video {video.title} not Exists')
            video.streams.filter(progressive=True).order_by('resolution').desc().first().download()
            print(f'Video {video.title} Downloaded')
        else:
            print(f'Video {video.title} Exists')
    print('Channel Video Download Complete')
    os.chdir(cd)

def chAudioClick():
    print('Channel Audio Download Button Clicked')
    channelAudioInput = txt.get()
    ch = Channel(channelAudioInput)
    print(f'Downloading videos by: {ch.channel_name}')
    print('Channel Video List')
    print(ch)
    if os.path.isdir(f'channel/{ch.channel_name}') == True :
        print(f'Channel {ch.channel_name} Folder Exists')
    else:
        os.mkdir(f'channel/{ch.channel_name}')
    if os.path.isdir(f'channel/{ch.channel_name}/Audio') == True :
        print(f'Channel {ch.channel_name} Audio Folder Exists')
    else :
        os.mkdir(f'channel/{ch.channel_name}/Audio')
    print('----')
    print('Channel Video Download Start')
    os.chdir(f'channel/{ch.channel_name}/Audio')
    for video in ch.videos:
        print('-------')
        print(video.title)
        if os.path.isfile(f'{video.title}.mp4') == False :
            print(f'Audio {video.title} not Exists')
            video.streams.filter(only_audio=True).get_audio_only().download()
            print(f'Audio {video.title} Downloaded')
        else:
            print(f'Audio {video.title} Exists')
    os.chdir(cd)
    print('Channel Audio Download Complete')

def selSingle():
    print('select Single')
def selChannel():
    print('select Channel')
def selAudio():
    print('select Audio')
def selVideo():
    print('select Video')
def DownloadClick():
    if var.get() == 1:
        print('Single Video')
        if VorA.get() == 1:
            print('Audio')
            AudioClick()
        elif VorA.get() == 2:
            print('Video')
            VideoClick()
    elif var.get() == 2:
        print('Channel Video')
        if VorA.get() == 1:
            print('Audio')
            chAudioClick()
        elif VorA.get() == 2:
            print('Video')
            chVideoClick()
    else:
        print('Nothing Selected')
    

root.title("Youtube Downloader")
root.configure(background='#f2f2f2')
lbl = tkinter.Label(root, text="URL", font=("Arial Bold", 16))
lbl.grid(row=1, column=0)
txt = tkinter.Entry(root, width=50, font=("Arial Bold", 16))
txt.grid(row=1, column=1)
download = tkinter.Button(root, text="Download", command=DownloadClick, font=("Arial Bold", 16))
download.grid(row=1, column=2)

var = IntVar()
VorA = IntVar()
R1 = tkinter.Radiobutton(root, text="Single", variable=var, value=1, command=selSingle)
R1.grid(row=4, column=0)
R2 = tkinter.Radiobutton(root, text="Channel", variable=var, value=2, command=selChannel)
R2.grid(row=5, column=0)
R3 = tkinter.Radiobutton(root, text="Audio", variable=VorA, value=1, command=selAudio)
R3.grid(row=4, column=1)
R4 = tkinter.Radiobutton(root, text="Video", variable=VorA, value=2, command=selVideo)
R4.grid(row=5, column=1)
root.mainloop()