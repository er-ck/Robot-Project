from Tkinter import *
import ttk

def buttonClick(arg):
	print "you passed" , arg


	
root = Tk()

root.title("Feet to Meters")

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

label = Label(root, text="this is a label")
label.pack()

button = Button(root, text="this is a button")
button.pack()

root.mainloop()