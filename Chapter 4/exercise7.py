from graphics import *
import math

def main() :

	# Create a graphics window with labels on left edge
	win = GraphWin("Circle Intersection", 640, 640)
	win.setBackground("white")
	win.setCoords(-10, -10, 10, 10)

	t1 = Text(Point(0, 8), "Welcome to this")
	t2 = Text(Point(0, 6), "Enter the values")
	t3 = Text(Point(0, -8), "Click anywhere to continue")

	# Ask user input on screen
	t4 = Text(Point(-2,2), "                Radius of the circle (between 0 and 10):")
	t5 = Text(Point(-2,0), "y-intercept of the horizontal line (between -10 and 10):")

	t1.draw(win)
	t2.draw(win)
	t3.draw(win)
	t4.draw(win)
	t5.draw(win)

	inputRadius = Entry(Point(6, 2), 5)
	inputRadius.setText("5.0")
	inputRadius.draw(win)

	inputY = Entry(Point(6, 0), 5)
	inputY.setText("2.0")
	inputY.draw(win)

	win.getMouse()

	# Undraw text
	t1.undraw()
	t2.undraw()
	t3.undraw()
	t4.undraw()
	t5.undraw()
	inputRadius.undraw()
	inputY.undraw()

	# Go to next screen
	r = float(inputRadius.getText())
	y = float(inputY.getText())

	# Draw the circle
	c = Circle(Point(0,0), r)
	c.draw(win)

	# Draw the horizontal line
	h = Line(Point(-10, y), Point(10, y))
	h.draw(win)

	# Compute intersection
	delta = r**2 - y**2

	if delta > 0:
		x = math.sqrt(r**2 - y**2)
		Text(Point(0, -8), "Intersections:").draw(win)
		Text(Point(0, -9), "{:.2f} and {:.2f}".format(x, -x)).draw(win)
		c1 = Circle(Point(-x, y), 0.2)
		c1.setFill("red")
		c1.draw(win)
		c2 = c1.clone()
		c2.move(2*x, 0)
		c2.draw(win)
	elif delta == 0:
		Text(Point(0, -8), "Intersections:").draw(win)
		Text(Point(0, -9), "0").draw(win)
	else:
		Text(Point(0, -8), "There are no intersections :(").draw(win)
	
	win.getMouse()
	win.close()
	
main()