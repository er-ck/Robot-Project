__author__ = 'Erick'

from Tkinter import *
from tkMessageBox import *

class Application(Frame):
    def __init__(self, frame):
        Frame.__init__(self, frame)
        self.pack()
        self.Widgets()



    def clicked(self, content):
        if content == "":
            showinfo("Clicked", "You typed nothing into the input box.")
        else:
            showinfo("Clicked", "You typed: " + content)

    def getGeometry(self, geo):
        print geo

    def Widgets(self):

        # Creates the input box.
        self.tbx = Entry(self)
        self.tbx.grid()

        # Creates the button that we click to show what we entered into the input box.
        self.btn = Button(self)
        self.btn['text'] = "Get!"
        self.btn['command'] = lambda: self.clicked(self.tbx.get())
        self.btn.grid(column=1, row=0)

        # Allows me to see the current screen resolution and the offset.
        self.geo = Button(self)
        self.geo['text'] = "Get geometry"
        self.geo['command'] = lambda: self.getGeometry(self.winfo_geometry())
        # self.geo.grid()





root = Tk()
root.title("Type and Print")
root.geometry("220x32")
Application(root)
mainloop()