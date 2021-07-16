from graphics import *

def main():
	win = GraphWin("Smiley", 400, 400)
	win.setCoords(-10, -10, 10, 10)
	
	bigCircle = Circle(Point(0, 0), 8)
	bigCircle.setFill("yellow")
	bigCircle.draw(win)

	mouthDown = Circle(Point(0, 0), 5.5)
	mouthDown.setWidth(6)
	mouthDown.setOutline("red")
	mouthDown.draw(win)

	mouthUp = Circle(Point(0, 1), 6)
	mouthUp.setFill("yellow")
	mouthUp.setOutline("yellow")
	mouthUp.draw(win)

	leftEye = Circle(Point(-3, 3), 1)
	leftEye.setFill("blue")
	leftEye.draw(win)

	rightEye = leftEye.clone()
	rightEye.move(6, 0)
	rightEye.draw(win)



	win.getMouse()
	win.close()
main()