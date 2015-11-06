# Purpose:
#   Use the GUI, WASD or the arrow keys to control the robots movement.

# Reason for updated version:
#   Reason for an updated version is that using the setWidgetProperties, I would be able to eliminate a lot of repeated
#   code and be able to set everything easily through one function therefore saving time & space.

# Notes:
#   This verison is just the barebones GUI with buttons not linked to actually move the robot.
#   Linking the buttons to pi2go module wouldn't take long.

# !/usr/bin/python

# Imports
__author__ = 'Erick Musembi'
__version__ = "1.2"
__date__ = "28th February 2015"

from Tkinter import *
# from tkMessageBox import showinfo#
# #import pi2go as pi


class Application(Frame):
    def __init__(self, window):
        # Creates the main frame for the window.
        Frame.__init__(self, window)
        self.pack()

        # Create the top  and bottom frames.
        # Top is for the status bar & distance.
        self.topFrame = Frame(self)
        self.topFrame.pack()

        # Bottom is for the buttons.
        self.bottomFrame = Frame(self)
        self.bottomFrame.pack()

        # Frame geometry button.
        self.btn_geometry = Button(self.bottomFrame)
        self.btn_geometry['anchor'] = E
        self.setWidgetProperties(self.btn_geometry,
                                 text="Geometry",
                                 foreground="red",
                                 command=lambda: self.getGeometry())
        self.btn_geometry.pack({'padx': 5})

        # The status header label.
        self.lbl_status_header = Label(self.topFrame)
        self.setWidgetProperties(self.lbl_status_header,
                                 text="Status:",
                                 foreground="black")
        self.lbl_status_header.grid(row=0, column=0)

        # The status label that will change to show the status of the robot.
        self.lbl_status = Label(self.topFrame)
        self.setWidgetProperties(self.lbl_status,
                                 text="Idle",
                                 foreground="red")
        self.lbl_status.grid(row=0, column=1, columnspan=2)

        # The distance header label.
        self.lbl_distance_header = Label(self.topFrame)
        self.setWidgetProperties(self.lbl_distance_header,
                                 text="Distance:",
                                 foreground="black")
        self.lbl_distance_header.grid(row=1, column=0)

        # The distance label that will change to show the distance of the nearest object to the robot.
        self.lbl_distance = Label(self.topFrame)
        self.setWidgetProperties(self.lbl_distance,
                                 text="# cm",
                                 foreground="red")
        self.lbl_distance.grid(row=1, column=1)

        # Creating the up, down, left and right buttons and adding padding & unicode so it looks a little but prettier.
        self.btn_left = Button(self.bottomFrame)
        self.setWidgetProperties(self.btn_left, text=u"\u2190 Left")
        self.btn_left.pack({'side': 'left', 'padx': 5})

        self.btn_right = Button(self.bottomFrame)
        self.setWidgetProperties(self.btn_right, text="Right " + u"\u2192")
        self.btn_right.pack({'side': 'right', 'padx': 5})

        self.btn_down = Button(self.bottomFrame)
        self.setWidgetProperties(self.btn_down, text=u"\u2193 Down")
        self.btn_down.pack({'side': 'bottom', 'pady': 5})

        self.btn_up = Button(self.bottomFrame)
        self.setWidgetProperties(self.btn_up, text=u"\u2191 Up", padX=10)
        self.btn_up.pack({'side': 'bottom', 'pady': 5})


    def getGeometry(self,):
        print self.winfo_geometry()

    # These aren't used yet but I made them because I know I'll use them when it come to making the buttons
    # work.
    def setDistanceText(self, text):
        self.lbl_distance['text'] = text

    def setStatusText(self, text):
        self.lbl_status['text'] = text

    def setWidgetProperties(self, Widget, text=None, background=None, foreground=None, command=None, boarderWidth=None, padX=None, padY=None):
        if text is not None:
            Widget['text'] = text
        if command is not None:
            Widget['command'] = command
        if boarderWidth is not None:
            Widget['boarderWidth'] = True
        if background is not None:
            Widget['bg'] = background
        if foreground is not None:
            Widget['fg'] = foreground
        if padX is not None:
            Widget['padx'] = padX
        if padY is not None:
            Widget['pady'] = padY


root = Tk()
# root.geometry("191x70")
Application(root)
mainloop()