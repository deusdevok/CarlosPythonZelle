from graphics import *

def main():
	win = GraphWin('Regression Line', 640, 640) # (0, 0) is in the upper left corner
	win.setCoords(0, 0, 100, 100)
	win.setBackground('#dedede')

	done = Rectangle(Point(2, 2), Point(20, 10))
	done.setFill('blue')
	done.setWidth(3)
	done.draw(win)

	t = Text(Point(11, 6), "Done")
	t.setSize(18)
	t.setStyle("bold")
	t.setTextColor("white")
	t.draw(win)

	xList = []
	yList = []

	p = win.getMouse()
	x, y = p.getX(), p.getY()

	while not (x >= 2 and x <= 20 and y >= 2 and y <= 10):
		c = Circle(p, 1)
		c.setFill('red')
		c.draw(win)

		xList.append(x)
		yList.append(y)

		p = win.getMouse()
		x, y = p.getX(), p.getY()

	# Number of points
	n = len(xList)

	xAverage, yAverage = sum(xList)/n, sum(yList)/n

	mNumerator = sum([i*j for i, j in zip(xList, yList)]) - n*xAverage*yAverage

	mDenominator = sum([i**2 for i in xList]) - n*xAverage**2

	m = mNumerator/mDenominator

	# Draw the regression line y = yAverage + m*(x - xAverage)
	p1 = Point(2, yAverage + m*(2 - xAverage))
	p2 = Point(98, yAverage + m*(98 - xAverage))

	regLine = Line(p1, p2)
	regLine.draw(win)


	# Wait for the user to click anywhere before exit
	win.getMouse()
	win.close()

if __name__ == '__main__':
	main()