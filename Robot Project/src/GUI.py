# Use the GUI, WASD or the arrow keys to control the robots movement.

# GUI 1.0 - This show up on the rasbperry pi when ran as: sudo python GUI.pi
# Discoveries are that if I import motor, the the functions execute & therefore the command line control works without
# showing the GUI.
# Solution is to not import the motor.py but to use it as guide for if I get stuck.

__author__ = 'Erick Musembi'
__date__ = '27th February 2015'

from Tkinter import *
from tkMessageBox import showinfo
# import pi2go
# from motor import *


class Window(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        self.pack()

        self.button = Button(self)
        self.button['text'] = "Button!"
        self.button['fg'] = "red"
        self.button['bg'] = "blue"
        self.button['command'] = self.click
        self.button.pack({'side': 'left'})

    def click(self):
        showinfo("click", "button has been clicked!")
        print "button has been clicked & registered."

root = Tk()
root.title("Robot GUI")
Window(root)
mainloop()

