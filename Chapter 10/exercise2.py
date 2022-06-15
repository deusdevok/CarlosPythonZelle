from graphics import *
from button import Button

def main():
	
	# Open the file
	infile = open("exercise2input.txt", "r")
	chars = infile.read()
	lines = chars.split('\n')
	numbers = list(map(int, lines))

	win = GraphWin("Exercise 16", 640, 480)

	mainButton = Button(win, Point(320, 240), 150, 30, "Start")
	mainButton.activate()

	pt = win.getMouse()
	while not mainButton.clicked(pt):
		pt = win.getMouse()

	mainButton.deactivate()

	numbersUnique = []

	for n in range(11):
		# Count how many times n appears in numbers
		numbersUnique.append(numbers.count(n))
	maxNum = max(numbersUnique)

	for n in range(11): # Range from 0 to 10

		message = Text(Point((n+1)*640/12, 440), str(n))
		message.setStyle("bold")
		message.setTextColor("blue")
		message.draw(win)

		shape = Rectangle(Point((n+1)*640/12-5, 420), Point((n+1)*640/12+5, 420-400*numbersUnique[n]/maxNum))
		shape.setOutline("red")
		shape.setFill("red")
		shape.draw(win)


	message = Text(Point(320, 470), "Click anywhere to quit")
	message.setStyle("bold")
	message.setTextColor("blue")
	message.draw(win)
	clickPoint = win.getMouse()
	win.close()
main()