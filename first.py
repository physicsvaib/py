#importing tkinter
from tkinter import *
#main functioning starts
class window(Frame):
    def __init__(self,master=NONE):
        Frame.__init__(self,master)
        self.master=master
        self.y()
    def y(self):
        self.master.title("hello again")
        self.pack(fill=BOTH,expand=6)
        quit=Button(self,text="quit",command=self.x)
        quit.place(x=0,y=0)
        menu=Menu(self.master)
        self.master.config(menu=menu)
        file=Menu(menu)
        file.add_command(label="menu",command=self.x)
        menu.add_cascade(label="file",menu=file)
        edit=Menu(menu)
        edit.add_command(label="edit",command=self.x)
        edit.add_command(label="new")
        menu.add_cascade(label="edit",menu=edit)
    def x(self):
        exit()
ro=Tk()
app1=window(ro)
ro.geometry('300x400')
ro.mainloop()
