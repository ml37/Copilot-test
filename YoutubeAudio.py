from pytube import YouTube
import ffmpeg
import tkinter
import os

root = tkinter.Tk()

def waClick():
    print("Button Clicked") 
    url = txt.get()
    print(url)
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).get_audio_only()
    stream.download()
    lbl2 = tkinter.Label(root, text="Download Complete", font=("Arial Bold", 20))
    lbl2.grid(column=0, row=1)
    print("Download Complete")
    

root.title("Youtube Audio Downloader")
root.configure(background='#f2f2f2')
lbl = tkinter.Label(root, text="URL", font=("Arial Bold", 20))
lbl.grid(column=0, row=0)
txt = tkinter.Entry(root, width=50, font=("Arial Bold", 20))
txt.grid(column=1, row=0)
btn = tkinter.Button(root, text="Download", font=("Arial Bold", 20), command=waClick)
btn.grid(column=2, row=0)

root.mainloop()