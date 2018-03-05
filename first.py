#importing tkinter
from tkinter import *
from PIL import Image,ImageTk
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
        edit.add_command(label="Show Image",command=self.show)
        edit.add_command(label="Show Text",command=self.showt)

        edit.add_command(label="new")
        menu.add_cascade(label="edit",menu=edit)
    def x(self):
        exit()
    def show(self):
        load=Image.open('a.jpg')
        render=ImageTk.PhotoImage(load)
        img=Label(self,image=render)
        img.image=render
        img.place(x=0,y=0)
    def showt(self):
        text=Label(self,text="hello there")
        text.pack()
ro=Tk()
app1=window(ro)
ro.geometry('300x400')
ro.mainloop()
