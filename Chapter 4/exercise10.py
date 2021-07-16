from graphics import *
import math

def main() :

	win = GraphWin("Triangle Information", 640, 640)
	win.setBackground("white")
	win.setCoords(-10, -10, 10, 10)

	t1 = Text(Point(0, 9), "Click three points on the screen please")
	t1.draw(win)

	p1 = win.getMouse()
	c1 = Circle(p1, 0.1)
	c1.setFill("red")
	c1.draw(win)

	p2 = win.getMouse()
	c2 = Circle(p2, 0.1)
	c2.setFill("red")
	c2.draw(win)

	p3 = win.getMouse()
	c3 = Circle(p3, 0.1)
	c3.setFill("red")
	c3.draw(win)

	x1 = p1.getX()
	x2 = p2.getX()
	x3 = p3.getX()
	y1 = p1.getY()
	y2 = p2.getY()
	y3 = p3.getY()

	# Draw triangle
	tri = Polygon(p1, p2, p3)
	tri.setFill("cyan")
	tri.draw(win)

	# Lengths
	a = math.sqrt((x2-x1)**2+(y2-y1)**2)
	b = math.sqrt((x2-x3)**2+(y2-y3)**2)
	c = math.sqrt((x1-x3)**2+(y1-y3)**2)

	# Area and Perimeter
	perimeter = a+b+c
	s = perimeter/2
	area = math.sqrt(s*(s-a)*(s-b)*(s-c))

	t2 = Text(Point(0, -8), "Area = {:.2f}, Perimeter = {:.2f}".format(area, perimeter))
	t2.draw(win)
	
	t3 = Text(Point(0, -9), "Click again to exit")
	t3.draw(win)
	win.getMouse()
	win.close()
	
main()