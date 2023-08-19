from graphics import *
from button import Button
import random

def main():
    win = GraphWin('Three Button Monte', 640, 480)

    # witdh and height of buttons
    w, h = 180, 80
    
    buttonOne = Button(win, Point(120, 240), w, h, 'Door 1')
    buttonTwo = Button(win, Point(320, 240), w, h, 'Door 2')
    buttonThree = Button(win, Point(520, 240), w, h, 'Door 3')

    buttonPlayAgain = Button(win, Point(120, 420), w, h, 'Play Again') # Initially inactive by default
    buttonQuit = Button(win, Point(520, 420), w, h, 'Quit')

    messageIntro = Text(Point(320, 100), 'Welcome to Three Button Monte Game!\nPick a door, try to guess.')
    messageIntro.draw(win)

    wins, losses = 0, 0

    while True:
        buttonQuit.activate()
        buttonOne.activate()
        buttonTwo.activate()
        buttonThree.activate()

        pt = win.getMouse()

        while not any([buttonOne.clicked(pt), buttonTwo.clicked(pt), buttonThree.clicked(pt), buttonQuit.clicked(pt)]):
            pt = win.getMouse()

        if buttonQuit.clicked(pt):
            win.close()
            break 
        
        # At this point, one of the three doors was chosen by the user
        if buttonOne.clicked(pt):
            b = 1
        elif buttonTwo.clicked(pt):
            b = 2
        else:
            b = 3

        r = random.choice([1, 2, 3])
        if b == r:
            result = 'You Won !! Good for you'
            wins += 1
        else:
            result = 'You Lost. Deal with it ...'
            losses += 1

        

        buttonOne.deactivate()
        buttonTwo.deactivate()
        buttonThree.deactivate()

        message = Text(Point(320, 340), 'You picked door number {}\n{}\nThe correct door was {}'.format(b, result, r))

        try:
            winsAndLosses.undraw()
        except:
            pass
        
        if wins > 0 or losses > 0:
            winsAndLosses = Text(Point(320, 420), 'Wins: {}\n\nLosses: {}'.format(wins, losses))
            winsAndLosses.draw(win)

        message.draw(win)

        buttonPlayAgain.activate()
        

        pt = win.getMouse()
        while not any([buttonPlayAgain.clicked(pt), buttonQuit.clicked(pt)]):
            pt = win.getMouse()

        if buttonPlayAgain.clicked(pt):
            message.undraw()

        if buttonQuit.clicked(pt):
            win.close()
            break
            

if __name__ == '__main__':
    main()