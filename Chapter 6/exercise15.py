from graphics import *

def drawFace(center, size, win):
	# size is the radius of the face (an int)

	bigCircle = Circle(center, size)
	bigCircle.setFill("yellow")
	bigCircle.draw(win)

	r = size/1.8
	mouthDown = Circle(center, r)
	mouthDown.setWidth(2*size)
	mouthDown.setOutline("red")
	mouthDown.draw(win)

	cX = center.getX()
	cY = center.getY()

	mouthUp = Polygon(Point(cX-r, cY), Point(cX-r, cY+r), 
		Point(cX+r, cY+r), Point(cX+r, cY))
	mouthUp.setFill("yellow")
	mouthUp.setOutline("yellow")
	mouthUp.setWidth(2*size)
	mouthUp.draw(win)

	leftEye = Circle(Point(cX-r/1.5, cY+r/1.5), size/10)
	leftEye.setFill("blue")
	leftEye.draw(win)

	rightEye = leftEye.clone()
	rightEye.move(2*r/1.5, 0)
	rightEye.draw(win)


def main():
	win = GraphWin("Smiley", 600, 600)
	win.setCoords(-10, -10, 10, 10)
	
	drawFace(Point(-8, -8), 2, win)
	drawFace(Point(7, 7), 1, win)
	drawFace(Point(0, 0), 5, win)
	drawFace(Point(-5, 7), 3, win)

	win.getMouse()
	win.close()
main()