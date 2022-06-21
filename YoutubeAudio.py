from pytube import YouTube
from pytube import Channel
import tkinter
import os
from os import path
import shutil

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
if os.path.isdir('channel/Audio') == True :
    print('channel Audio Folder Already Exists')
else:
    os.mkdir('channel/Audio')
if os.path.isdir('channel/Video') == True :
    print('channel Video Folder Already Exists')
else:
    os.mkdir('channel/Video')

def AudioClick():
    status.config(text="Audio Downloading...")
    print("Audio Download Button Clicked") 
    urlInput = txt.get()
    print(urlInput)
    yt = YouTube(urlInput)
    stream = yt.streams.filter(only_audio=True).get_audio_only()
    stream.download()
    shutil.move(f'{yt.title}.mp4', f'Audio/{yt.title}.mp4')
    status.config(text="Downloaded")
    print("Download Complete")

def VideoClick():
    status.config(text="Video Downloading...")
    print("Video Download Button Clicked")
    urlInput = txt.get()
    print(urlInput)
    yt = YouTube(urlInput)
    stream = yt.streams.filter(progressive=True).order_by('resolution').desc().first()
    stream.download()
    shutil.move(f'{yt.title}.mp4', f'Video/{yt.title}.mp4')
    status.config(text="Downloaded")
    print("Download Complete")

def chVideoClick():
    print('Channel Download Button Clicked')
    channelInput = txt2.get()
    ch = Channel(channelInput)
    print(f'Downloading videos by: {ch.channel_name}')
    print('Channel Video List')
    print(ch)
    if os.path.isdir(f'channel/Video/{ch.channel_name}') == True :
        print(f'Channel {ch.channel_name} Folder Exists')
    else :
        os.mkdir(f'channel/Video/{ch.channel_name}')
    print('----')
    print('Channel Video Download Start')
    os.chdir(f'channel/Video/{ch.channel_name}')
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
    channelAudioInput = txt2.get()
    ch = Channel(channelAudioInput)
    print(f'Downloading videos by: {ch.channel_name}')
    print('Channel Video List')
    print(ch)
    if os.path.isdir(f'channel/Audio/{ch.channel_name}') == True :
        print(f'Channel {ch.channel_name} Folder Exists')
    else :
        os.mkdir(f'channel/Audio/{ch.channel_name}')
    print('----')
    print('Channel Video Download Start')
    os.chdir(f'channel/Audio/{ch.channel_name}')
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

root.title("Youtube Downloader")
root.configure(background='#f2f2f2')
lbl = tkinter.Label(root, text="URL", font=("Arial Bold", 16))
lbl.grid(row=1, column=0)
lbl2 = tkinter.Label(root, text="Channel", font=("Arial Bold", 16))
lbl2.grid(row=2, column=0)
status = tkinter.Label(root, text="Ready", font=("Arial Bold", 16))
status.grid(row=0, column=1)
txt = tkinter.Entry(root, width=50, font=("Arial Bold", 16))
txt.grid(row=1, column=1)
txt2 = tkinter.Entry(root, width=50, font=("Arial Bold", 16))
txt2.grid(row=2, column=1)
btn = tkinter.Button(root, text="Audio", font=("Arial Bold", 16), background='#818D92',command=AudioClick)
btn.grid(row=1, column=2)
btn2 = tkinter.Button(root, text="Video", font=("Arial Bold", 16), background='#818D92',command=VideoClick)
btn2.grid(row=1, column=3)
btn3 = tkinter.Button(root, text='Audio', font=("Arial Bold", 16), background='#818D92', command=chAudioClick)
btn3.grid(row=2, column=2)
btn4 = tkinter.Button(root, text='Video', font=("Arial Bold", 16), background='#818D92', command=chVideoClick)
btn4.grid(row=2, column=3)

root.mainloop()