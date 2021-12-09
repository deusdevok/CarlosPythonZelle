from graphics import *

def moveTo(shape, newCenter):
	# Moves shape so that newCenter is its center.
	# shape: graphics object that supports the getCenter method.
	# newCenter: a Point object.
	c = shape.getCenter()
	shape.move(newCenter.getX()-c.getX(), newCenter.getY()-c.getY())

def main():
	win = GraphWin("Move circle", 600, 600)
	win.setCoords(-10,-10,10,10)
	c = Circle(Point(0,0), 2) # Initial circle
	c.draw(win)

	for _ in range(10):
		pCenter = win.getMouse()
		moveTo(c, pCenter)

	win.getMouse()
	win.close()

main()