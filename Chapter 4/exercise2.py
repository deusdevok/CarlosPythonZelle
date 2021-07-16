from graphics import *

def main():
	win = GraphWin("Archery Target", 400, 400)
	win.setBackground("gray")

	r = [200, 160, 120, 80, 40]
	colors = ["white", "black", "blue", "red", "yellow"]
	for i in range(5):
		c = Circle(Point(200, 200), r[i])
		c.setFill(colors[i])
		c.setOutline(colors[i])
		c.draw(win)
	win.getMouse()
	win.close()
main()