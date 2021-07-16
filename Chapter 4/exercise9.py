from graphics import *

def main() :

	
	win = GraphWin("Rectangle Information", 640, 640)
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

	# Draw rectangle
	rect = Rectangle(p1, p2)
	rect.setFill("cyan")
	rect.draw(win)

	# Length and Width
	length = abs(x2-x1)
	width = abs(y2-y1)

	# Area and Perimeter
	area = length*width
	perimeter = 2*(length+width)

	t2 = Text(Point(0, -8), "Area = {:.2f}, Perimeter = {:.2f}".format(area, perimeter))
	t2.draw(win)
	
	t3 = Text(Point(0, -9), "Click again to exit")
	t3.draw(win)
	win.getMouse()
	win.close()
	
main()