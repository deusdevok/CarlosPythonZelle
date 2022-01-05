from graphics import *

def main():
	win = GraphWin("Bouncing Ball", 300, 200, autoflush=False)
	win.setBackground('gray')

	radius = 30
	c = Circle(Point(radius+1, radius+1), radius)
	c.setFill('red')
	c.setOutline('blue')
	c.draw(win)

	dx = 1
	dy = 1

	for _ in range(1500):
		p = c.getCenter()
		x, y = p.getX(), p.getY()

		if x+radius >= 300 or x-radius <= 0:
			dx = -dx
		if y+radius >= 200 or y-radius <= 0:
			dy = -dy

		c.move(dx, dy)
		update(120)

	# Wait for the user to click before exiting
	win.getMouse()
	win.close()

if __name__ == '__main__':
	main()