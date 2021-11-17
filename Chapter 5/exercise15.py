from graphics import *

def main():
	

	# Open the file
	infile = open("exercise15input.txt", "r")
	chars = infile.read()
	lines = chars.split('\n')
	numberOfStudents = int(lines[0])

	win = GraphWin("Exercise 15", 640, numberOfStudents*70)

	i = 0
	for line in lines[1:]:
		name, score = line.split()
		score = float(score)

		message = Text(Point(140, (i+1)*50), name.ljust(20))
		message.setStyle("bold")
		message.setTextColor("blue")
		message.draw(win)

		shape = Rectangle(Point(300, (i+1)*50-10), Point(300+score*3, (i+1)*50+10))
		shape.setOutline("red")
		shape.setFill("red")
		shape.draw(win)

		i += 1


	message = Text(Point(320, (i+1)*50+10), "Click anywhere to quit")
	message.setStyle("bold")
	message.setTextColor("blue")
	message.draw(win)
	clickPoint = win.getMouse()
	win.close()
main()