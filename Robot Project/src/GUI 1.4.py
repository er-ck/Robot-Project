# Purpose:
#   Use the GUI, WASD or the arrow keys to control the robots movement.

# Reason for update:
#   Leaving a basic GUI (v1.2) for anyone who would ever need it for the
#   same/similar project.

# Notes:
#

#!/usr/bin/python

# Imports
__author__ = 'Erick Musembi'
__version__ = "1.4"
__date__ = "19th March 2015"

from Tkinter import *
from tkMessageBox import showinfo, showerror
#import pi2go
#import motor as m

# Variables:
UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3
SPEED = 30
DISTANCE = 0
# Counter for the number of times that the distance is updated.
count = 0


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
        self.lbl_status.grid(row=0, column=1, columnspan=1)

        # The distance header label.
        self.lbl_distance_header = Label(self.topFrame)
        self.setWidgetProperties(self.lbl_distance_header,
                                 text="Distance:",
                                 foreground="black")
        self.lbl_distance_header.grid(row=1, column=0)

        # The distance label that will change to show the distance of the nearest object to the robot.
        self.lbl_distance = Label(self.topFrame)
        self.setWidgetProperties(self.lbl_distance,
                                 text="## cm",
                                 foreground="red")
        self.lbl_distance.grid(row=1, column=1, columnspan=1, padx=3)

        # Creating the up, down, left and right buttons and adding padding & unicode so it looks a little but prettier.
        self.btn_left = Button(self.bottomFrame)
        self.setWidgetProperties(self.btn_left, text=u"\u2190 Left", command=lambda: self.buttonPress(LEFT, SPEED))
        self.btn_left.bind('a', lambda: self.buttonPress(LEFT, 10))
        self.btn_left.pack({'side': 'left', 'padx': 5})

        self.btn_right = Button(self.bottomFrame)
        self.setWidgetProperties(self.btn_right, text="Right " + u"\u2192", command=lambda: self.buttonPress(RIGHT, SPEED))
        self.btn_right.pack({'side': 'right', 'padx': 5})

        self.btn_down = Button(self.bottomFrame)
        self.setWidgetProperties(self.btn_down, text=u"\u2193 Down", command=lambda: self.buttonPress(DOWN, SPEED))
        self.btn_down.pack({'side': 'bottom', 'pady': 5})

        self.btn_up = Button(self.bottomFrame)
        self.setWidgetProperties(self.btn_up, text=u"\u2191 Up", padX=10, command=lambda: self.buttonPress(UP, SPEED))
        self.btn_up.pack({'side': 'bottom', 'pady': 5})

        #self.speed_scroll = Scale(self.topFrame)
        #self.speed_scroll.grid(column=4, row=0)

        self.run()


    def buttonPress(self, direction, speed, event=None):
        if direction == UP:
            self.setStatusText("Moving forward")
            pi2go.forward(speed)
        elif direction == DOWN:
            self.setStatusText("Moving backwards")
            pi2go.reverse(speed)
        elif direction == LEFT:
            self.setStatusText("Spinning left (anticlockwise)")
            pi2go.spinRight(speed)
        elif direction == RIGHT:
            self.setStatusText("Moving right (clockwise)")
            pi2go.spinLeft(speed)
        else:
            self.setStatusText("ERROR!")
            pi2go.cleanup()
            showerror("buttonPress() - distance: argument is invalid.")


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

    def refresh(self):
        global count
        count += 1
        ## Uncomment this on to enable distance updating.
        #DISTANCE = pi2go.getDistance()
        #self.setDistanceText(DISTANCE, " cm")
        print "Update has been updated ", count, " times."
        root.after(2000, self.refresh)
        
    def run(self):
        self.after(2000, self.refresh)
        self.mainloop()
        

root = Tk()
#root.geometry("191x70")
Application(root)
