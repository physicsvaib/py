# tkinter tutorials
from tkinter import *


class window(Frame):
    def __init__(x, master=None):
        Frame.__init__(x, master)
        x.y()

    def y(x):
        x.master.title("new program")
        x.pack(fill=BOTH, expand=6)
        quit = Button(x, text="quit", command=x.exit)
        quit.place(x=0, y=0)
        m=Menu(x.master)
        x.master.config(m=m)
        file=Menu(m)
        file.add_command(label='exit',command=x.exit)
        m.add_cascade(label='file',m=file)
        edit=Menu(m)
        edit.add_command(label="save",command=x.exit)
        edit.add_command(label='undo')
        m.add_cascade(label='edit',m=edit)
    def exit(self):
        exit()


root = Tk()
root.geometry("500x300")
app = window(root)
root.mainloop()
