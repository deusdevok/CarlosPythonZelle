from graphics import *

def main():
	win = GraphWin()
	shape = Rectangle(Point(50, 50), Point(80, 80))
	shape.setOutline("red")
	shape.setFill("red")
	shape.draw(win)
	for i in range(10):
		p = win.getMouse()
		c = shape.getCenter()

		dx = p.getX() - c.getX()
		dy = p.getY() - c.getY()

		shapeCopy = shape.clone()
		shapeCopy.move(dx, dy)

		shapeCopy.draw(win)

	message = Text(Point(100, 100), "Click again to quit")
	message.setStyle("bold")
	message.setTextColor("blue")
	message.draw(win)
	clickPoint = win.getMouse()
	win.close()
main()