# Pi2Go basic motor sketch - for the first episode of my robot tutorial series.
# In truth this program is very simple - the parts where it captures key presses is the daunting bit.
# Try to work through it slowly and you'll soon understand!

# Use the arrow keys to control the direction of the Pi2Go and use the 'greater than' and 'less than'
# keys to edit the SPEED!

import pi2go, time

# Reading a button press from your keyboard, don't worry about this too much!
import sys
import tty
import termios

UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3
SPEED = 30

class Motor():
    def __init__(self):
        pi2go.init()
        
        # Main body of code - this detects your key press and changes direction depending on it.
        
        try:
            while True:
                keyp = self.readkey
                if keyp == 'w' or keyp == UP:
                    pi2go.forward(SPEED)
                    print 'Forward', SPEED
                elif keyp == 's' or keyp == DOWN:
                    pi2go.reverse(SPEED)
                    print 'Backward', SPEED
                elif keyp == 'd' or keyp == RIGHT:
                    pi2go.spinRight(SPEED)
                    print 'Spin Right', SPEED
                elif keyp == 'a' or keyp == LEFT:
                    pi2go.spinLeft(SPEED)
                    print 'Spin Left', SPEED
                elif keyp == '.' or keyp == '>':
                    SPEED = min(100, SPEED+10)
                    print 'SPEED+', SPEED
                elif keyp == ',' or keyp == '<':
                    SPEED = max (0, SPEED-10)
                    print 'SPEED-', SPEED
                elif keyp == ' ':
                    pi2go.stop()
                    print 'Stop'
                elif ord(keyp) == 3:
                    break

            # When you want to exit - press ctrl+c and it will generate a keyboard interrupt - this is handled nicely here!
        except KeyboardInterrupt:
                pi2go.cleanup()
                
    def readchar(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        if ch == '0x03':
            raise KeyboardInterrupt
        return ch

    def readkey(self):
        def readkey(getchar_fn=None):
            getchar = getchar_fn or readchar
            c1 = getchar()
            if ord(c1) != 0x1b:
                return c1
            c2 = getchar()
            if ord(c2) != 0x5b:
                return c1
            c3 = getchar()
            return ord(c3) - 65  # 0=Up, 1=Down, 2=Right, 3=Left arrows
        
