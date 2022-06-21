from pytube import YouTube
from pytube import Channel
import tkinter
import os
from os import path
import shutil

cd =os.getcwd()
print(f'start position {cd}')
root = tkinter.Tk()
if os.path.isdir('Audio') == True :
    print('Audio Folder Exists')
else:
    os.mkdir('Audio')
if os.path.isdir('Video') == True :
    print('Video Folder Exists')
else:
    os.mkdir('Video')
if os.path.isdir('channel') == True :
    print('channel Folder Exists')
else:
    os.mkdir('channel')



def AudioClick():
    #os.mkdir('Audio')
    lbl2.config(text="Audio Downloading...")
    print("Audio Download Button Clicked") 
    urlInput = txt.get()
    print(urlInput)
    yt = YouTube(urlInput)
    stream = yt.streams.filter(only_audio=True).get_audio_only()
    stream.download()
    shutil.move(f'{yt.title}.mp4', f'Audio/{yt.title}.mp4')
    lbl2.config(text="Downloaded")
    print("Download Complete")

def chClick():
    print('Channel Download Button Clicked')
    channelInput = txt.get()
    print('----')
    print(channelInput)
    ch = Channel(channelInput)
    print('----')
    print(f'Downloading videos by: {ch.channel_name}')
    print('Channel Video List')
    print(ch)
    if os.path.isdir(f'channel/{ch.channel_name}') == True :
        print(f'Channel {ch.channel_name} Folder Exists')
    else :
        os.mkdir(f'channel/{ch.channel_name}')
    print('----')
    print('Channel Video Download Start')
    os.chdir(f'channel/{ch.channel_name}')
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

def VideoClick():
    lbl2.config(text="Video Downloading...")
    print("Video Download Button Clicked")
    urlInput = txt.get()
    print(urlInput)
    yt = YouTube(urlInput)
    stream = yt.streams.filter(progressive=True).order_by('resolution').desc().first()
    stream.download()
    shutil.move(f'{yt.title}.mp4', f'Video/{yt.title}.mp4')
    lbl2.config(text="Downloaded")
    print("Download Complete")

root.title("Youtube Downloader")
root.configure(background='#f2f2f2')
lbl = tkinter.Label(root, text="URL", font=("Arial Bold", 20))
lbl.grid(row=0, column=2)
txt = tkinter.Entry(root, width=50, font=("Arial Bold", 20))
txt.grid(column=0, row=0)
btn = tkinter.Button(root, text="Audio", font=("Arial Bold", 20), background='#818D92',command=AudioClick)
btn.grid(row=1, column=1)
btn2 = tkinter.Button(root, text="Video", font=("Arial Bold", 20), background='#818D92',command=VideoClick)
btn2.grid(row=1, column=2)
btn3 = tkinter.Button(root, text='Channel', font=("Arial Bold", 20), background='#818D92', command=chClick)
btn3.grid(row=1, column=3)
lbl2 = tkinter.Label(root, text="Ready", font=("Arial Bold", 20))
lbl2.grid(row=1, column=0)
root.mainloop()