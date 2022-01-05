from graphics import *
import math, time

def main():
	win = GraphWin("Archery Target", 400, 500)
	win.setBackground("gray")

	r = [200, 160, 120, 80, 40]
	colors = ["white", "black", "blue", "red", "yellow"]
	for i in range(5):
		c = Circle(Point(200, 200), r[i])
		c.setFill(colors[i])
		c.setOutline(colors[i])
		c.draw(win)

	scores = []

	t1 = Text(Point(200, 450), "Game on!!!")
	t1.setSize(14)
	t1.setStyle('bold')
	t1.setTextColor('black')
	t1.draw(win)

	for _ in range(5):
		p1 = win.getMouse()
		c1 = Circle(p1, 2.5)
		c1.setFill("pink")
		c1.draw(win)

		x1 = p1.getX()
		y1 = p1.getY()

		r1 = math.sqrt((x1-200)**2 + (y1-200)**2)

		if r1 <= 40:
			score = 9
		elif r1 <= 80:
			score = 7
		elif r1 <= 120:
			score = 5
		elif r1 <= 160:
			score = 3
		elif r1 <= 200:
			score = 1
		else:
			score = 0

		scores.append(score)

		t1.undraw()
		if score > 0:
			t1 = Text(Point(200, 450), "You got {} points".format(score))
		else:
			t1 = Text(Point(200, 450), "You got {} points\nMan you suck...".format(score))
		t1.setSize(14)
		t1.setStyle('bold')
		t1.setTextColor('black')
		t1.draw(win)

	time.sleep(1)
	t1.undraw()
	t1 = Text(Point(200, 450), "Total score: {}\nClick anywhere to exit.".format(sum(scores)))
	t1.setSize(14)
	t1.setStyle('bold')
	t1.setTextColor('black')
	t1.draw(win)

	win.getMouse()
	win.close()

main()