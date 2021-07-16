from graphics import *

def main():
	win = GraphWin("Dice", 500, 500)
	win.setCoords(0, 0, 60, 60)
	win.setBackground(color_rgb(189,238,246))
	y1, y2 = 26, 34

	dice1 = Rectangle(Point(10*1-4,y1), Point(10*1+4,y2))
	dice1.setFill("white")
	Circ1 = Circle(Point(10*1, 30), 1)
	Circ1.setFill("red")

	dice2 = Rectangle(Point(10*2-4,y1), Point(10*2+4,y2))
	dice2.setFill("white")
	Circ21 = Circle(Point(10*2-1.5, 30+1.5), 1)
	Circ21.setFill("red")
	Circ22 = Circle(Point(10*2+1.5, 30-1.5), 1)
	Circ22.setFill("red")

	dice3 = Rectangle(Point(10*3-4,y1), Point(10*3+4,y2))
	dice3.setFill("white")
	Circ31 = Circle(Point(10*3-2, 30+2), 1)
	Circ31.setFill("red")
	Circ32 = Circle(Point(10*3, 30), 1)
	Circ32.setFill("red")
	Circ33 = Circle(Point(10*3+2, 30-2), 1)
	Circ33.setFill("red")

	dice4 = Rectangle(Point(10*4-4,y1), Point(10*4+4,y2))
	dice4.setFill("white")
	Circ41 = Circle(Point(10*4-1.5, 30+1.5), 1)
	Circ41.setFill("red")
	Circ42 = Circle(Point(10*4+1.5, 30+1.5), 1)
	Circ42.setFill("red")
	Circ43 = Circle(Point(10*4-1.5, 30-1.5), 1)
	Circ43.setFill("red")
	Circ44 = Circle(Point(10*4+1.5, 30-1.5), 1)
	Circ44.setFill("red")

	dice5 = Rectangle(Point(10*5-4,y1), Point(10*5+4,y2))
	dice5.setFill("white")
	Circ51 = Circle(Point(10*5-2, 30+2), 1)
	Circ51.setFill("red")
	Circ52 = Circle(Point(10*5+2, 30+2), 1)
	Circ52.setFill("red")
	Circ53 = Circle(Point(10*5-2, 30-2), 1)
	Circ53.setFill("red")
	Circ54 = Circle(Point(10*5+2, 30-2), 1)
	Circ54.setFill("red")
	Circ55 = Circle(Point(10*5, 30), 1)
	Circ55.setFill("red")

	dice1.draw(win)
	dice2.draw(win)
	dice3.draw(win)
	dice4.draw(win)
	dice5.draw(win)

	Circ1.draw(win)

	Circ21.draw(win)
	Circ22.draw(win)

	Circ31.draw(win)
	Circ32.draw(win)
	Circ33.draw(win)

	Circ41.draw(win)
	Circ42.draw(win)
	Circ43.draw(win)
	Circ44.draw(win)

	Circ51.draw(win)
	Circ52.draw(win)
	Circ53.draw(win)
	Circ54.draw(win)
	Circ55.draw(win)

	win.getMouse()
	win.close()
main()