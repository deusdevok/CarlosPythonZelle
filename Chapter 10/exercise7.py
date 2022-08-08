# Graphics program to roll a pair of circular dice. 
# Uses custom widgets Button and DieView.

from random import randrange
from graphics import GraphWin, Point

from cbutton import CButton
from dieview import DieView 

def main():

    # create the application window
    win = GraphWin("Dice Roller")
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")

    # Draw the interface widgets
    die1 = DieView(win, Point(3,7), 2)
    die2 = DieView(win, Point(7,7), 2)
    rollButton = CButton(win, Point(2,2), 1.7, "Roll Dice")
    rollButton.activate()
    quitButton = CButton(win, Point(8,2), 1.7, "Quit")

    # Event loop
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):
            value1 = randrange(1,7)
            die1.setValue(value1)
            value2 = randrange(1,7)
            die2.setValue(value2)
            quitButton.activate()
        pt = win.getMouse()

    # close up shop
    win.close()

main()
