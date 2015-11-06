# Use the GUI, WASD or the arrow keys to control the robots movement.

# maybe make functions that set all of the properties for the widgets by allowing params to be pushed into the function
# then checking if each one is None, if so, you don't change it but if its not None, you change it to whatever the value
# that has been passed into the function is.

# Why? hopefully this would save time rather than typing the same thing over and over again for each button.
# Instead of typing the same thing, I can init the functions in __init__ then just change their properties using the
# created function in createWidgets().

__author__ = 'Erick Musembi'
__version__ = '1.1'
__date__ = "28th February 2015"

# Imports
from Tkinter import *
# from tkMessageBox import showinfo
# import pi2go as pi


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

        # For debugging and making sure that I get a good window size.
        self.btn_geometry = Button(self.bottomFrame)
        self.btn_geometry['text'] = "Geometry"
        self.btn_geometry['command'] = lambda: self.getGeometry(self.winfo_geometry())
        self.btn_geometry.grid(row=0, column=0)

        # By using the new function, I can all of the properties as this:
        # self.setWidgetProperties(self.btn_geometry,
        #                          text="Btn Geometry",
        #                          command=lambda: self.getGeometry(self.winfo_geometry()),
        #                          foreground="green", background="red",
        #                          padX=10, padY=10)

        self.lbl_status_header = Label(self.topFrame)
        self.setWidgetText(self.lbl_status_header, "Status:")
        self.lbl_status_header['fg'] = "red"
        self.lbl_status_header.grid(sticky=E, column=2, row=0)

        self.lbl_status = Label(self.topFrame)
        self.setWidgetText(self.lbl_status, "test")
        self.lbl_status.grid(sticky=E, column=3, row=0, columnspan=2)



    def setWidgetText(self, Widget, text):
        Widget['text'] = text

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

    def getGeometry(self, geometry):
        print geometry


root = Tk()
root.title("Robot GUI")
Application(root)
mainloop()
