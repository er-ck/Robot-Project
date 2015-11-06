
from Tkinter import *
from tkMessageBox import *

class Window(Frame):
    def callback(self):
        showinfo("Callback", "callback has been called!")
		
	def __init__(self, frame):
		Frame.__init__(self, frame)
		self.pack()
		
        label = Label(self, text="GUI connecting to RPi")
        label.pack()
		        
    def createWidgets(self):
		button = Button(self, text="button")
		button.pack()
	
    


        
root = Tk()
Window(root)
mainloop()