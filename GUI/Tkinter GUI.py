from Tkinter import *
from tkMessageBox import *

def sender(sender):
    print "A event has occured, you have been sent here by the component with id: " + sender
def callback():
    print "Callback called"
    showinfo("Callback", "callback has been called!")

def help():
    print "Help has been clicked"

def exit():
    sys.exit()

root = Tk()

# create the menu and link it to the main window (Frame).
menu = Menu(root)
# configure the frame to allow the menu to show.
root.config(menu=menu)

# Create the menu so that we can add components
filemenu = Menu(menu)

# adds a cascade (a dropdown level)
menu.add_cascade(label="File", menu = filemenu)
#adds each button, giving them their name and the function that should be called when clicked.
filemenu.add_command(label="New", command=callback)
filemenu.add_command(label="Open", command=callback)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", command=sender("Help_btn1"))
helpmenu.add_command(label="About...", command=callback)

button = Button(root, text="Click me!", command=callback)
button.pack()

frame = Frame(root, height=200, width=100)

mainloop()
