from re import T
from tkinter import *
import asyncio
root = Tk()
root.title('root')
root.configure(background='black')

def onClick():
    name = txt.get()
    print(name)
    wa = Tk()
    wa.title('walalaru')
    wa.geometry('500x500')
    wa.configure(background='blue')
    wa.mainloop()

txt = Entry(root)
txt.grid(row=0, column=0)
btn = Button(root, text='OK', command=onClick)
btn.grid(row=0, column=1)
frame = Frame(root)
frame.grid(row=1, column=0)

root.mainloop()

