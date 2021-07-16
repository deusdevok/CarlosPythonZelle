from graphics import *
import math

def main() :

	
	win = GraphWin("Line Segment Information", 640, 640)
	win.setBackground("white")
	win.setCoords(-10, -10, 10, 10)

	t1 = Text(Point(0, 9), "Click two points on the screen please")
	t1.draw(win)

	p1 = win.getMouse()
	c1 = Circle(p1, 0.1)
	c1.setFill("blue")
	c1.draw(win)

	p2 = win.getMouse()
	c2 = Circle(p2, 0.1)
	c2.setFill("red")
	c2.draw(win)

	x1 = p1.getX()
	x2 = p2.getX()
	y1 = p1.getY()
	y2 = p2.getY()

	# Midpoint
	midX, midY = (x1+x2)/2, (y1+y2)/2
	m = Circle(Point(midX, midY), 0.2)
	m.setFill("cyan")
	m.draw(win)

	# Draw line
	l = Line(p1, p2)
	l.draw(win)

	# Length and slope
	dx = x2-x1
	dy = y2-y1
	length = math.sqrt(dx**2 + dy**2)
	slope = dy/dx

	t2 = Text(Point(0, -8), "Length = {:.2f}, Slope = {:.2f}".format(length, slope))
	t2.draw(win)
	
	t3 = Text(Point(0, -9), "Click again to exit")
	t3.draw(win)
	win.getMouse()
	win.close()
	
main()