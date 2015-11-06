from Tkinter import *
from tkMessageBox import *


class Application(Frame):
    def __init__(self, handle):
        Frame.__init__(self, handle)

        # Sets the geometry of the window.
        handle.geometry("300x250")

        self.button = Button(handle)
        self.button['text'] = "This is a button"
        self.button.bind('<Button-2>', lambda event: self.printmsg(event, "click"))
        #self.button['command'] = self.printmsg
        self.button.grid(row=2, column=5)

    def printmsg(self, event, message):
        showinfo("Click", "The button has been clicked!")
        print "A button has been clicked."
        print event
        print message

root = Tk()
Application(root)
mainloop()
