from re import T
from tkinter import *
import asyncio
root = Tk()
root.title('root')
root.geometry('500x500')
root.configure(background='black')
def onClick():
    name = txt.get()
    print(name)

txt = Entry(root)
txt.grid(row=0, column=1)
btn = Button(root, text='Click Me', command=onClick)
btn.grid(row=1, column=1)

root.mainloop()

wa = Tk()
wa.title('walalaru')
wa.geometry('500x500')
wa.configure(background='blue')
img = PhotoImage(file='serika.png')
imgLbl = Label(wa, image=img)
imgLbl.image = img
imgLbl.place(x=0, y=0)
wa.mainloop()