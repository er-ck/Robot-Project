from Tkinter import *
import ttk
root = Tk()

def printt(msg):
    print msg

ttk.Button(root, text="Hello World", command= lambda: printt('ping').grid())
root.mainloop()
