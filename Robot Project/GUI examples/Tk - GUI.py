from Tkinter import *
from tkMessageBox import *

class Application(Frame):
    def clicked(self, button):
        print "You clicked on button:", button
        
    def close(self):
        self.destroy

    def createWidgets(self):
        
        # creates the quit button.
        self.QUIT = Button(self)
        # sets the text.
        self.QUIT["text"] = "QUIT"
        # changes the foreground colour to red.
        self.QUIT["fg"]   = "red"
        # sets the command that is executed when clicked.
        self.QUIT["command"] =  self.quit
        # packs it to the window.
        #self.QUIT.pack({"side": "left"})

        # button on the left hand side.
        self.hi_there = Button(self)
        self.hi_there["text"] = "Left"
        self.hi_there["command"] = lambda : showinfo("title", "message")
        self.hi_there.pack({"side": "left", "padx":"5", "pady":"5"})

        # button on the right hand side.
        self.btn_one = Button(self)
        self.btn_one["text"] = "Right"
        self.btn_one["command"] = lambda: self.clicked("One")
        self.btn_one.pack({"side": "right", "pady":"5", "padx":"5"})

        # button at the bottom.
        self.btn_two = Button(self)
        self.btn_two["text"] = "Backwards"
        self.btn_two["command"] = lambda: self.clicked("Two")
        self.btn_two.pack({"side": "bottom", "pady":"5", "padx":"5"})

        # button in the middle.
        self.btn_two = Button(self)
        self.btn_two["text"] = "Stop"
        self.btn_two["command"] = lambda: self.clicked("Three")
        self.btn_two.pack({"side": "bottom", "pady":"5", "padx":"5"})

        # button at the top.
        self.btn_two = Button(self)
        self.btn_two["text"] = "Forwards"
        self.btn_two["command"] = lambda: self.clicked("Four")
        self.btn_two.pack({"side": "top", "pady":"5", "padx":"5"})

        # sequence could be seen as the following instructions:
        #   add something to the:
        #       1. left, 2. right, 3. bottomn 4. middle, 5. top
        # like filling a glass of water, the sides are filled first then from the bottom upwards.
        
	

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
root = Tk()
root.title("Robot GUI")
app = Application(master=root)
app.mainloop()
root.destroy()
