from graphics import *

def main():
	win = GraphWin("Five-click House", 640, 640)
	win.setBackground("white")
	win.setCoords(-10, -10, 10, 10)

	t1 = Text(Point(0, 9), "Click five times to draw a house :)")
	t1.draw(win)
	t2 = Text(Point(0, 8), "Let's start with the frame of the house. Click somewhere...")
	t2.draw(win)

	# Rectangular frame of the house
	p1 = win.getMouse()
	c1 = Circle(p1, 0.1)
	c1.setFill("Blue")
	c1.draw(win)

	t2.setText("Click one more time to draw the frame...")
	p2 = win.getMouse()

	while abs(p1.getX()-p2.getX()) < 5 or abs(p1.getY()-p2.getY()) < 5:
		#print(abs(p1.getX()-p2.getX()))
		#print(abs(p1.getY()-p2.getY()))
		t2.setText("Click further to make the frame bigger. Try again.")
		p2 = win.getMouse()

	c2 = Circle(p2, 0.1)
	c2.setFill("Blue")
	c2.draw(win)

	rect = Rectangle(p1, p2)
	rect.draw(win)

	# Door
	t2.setText("Click inside to draw a door (top edge)...")
	doorP = win.getMouse() # Center of the top edge of the door
	while doorP.getX() > max(p1.getX(), p2.getX()) or \
		doorP.getX() < min(p1.getX(), p2.getX()) or \
		doorP.getY() < min(p1.getY(), p2.getY()) or \
		doorP.getY() > max(p1.getY(), p2.getY()):
		t2.setText("The door should be inside the house, man...")
		doorP = win.getMouse()

	doorW = abs(p1.getX()-p2.getX())/5 # Door width
	door = Rectangle(Point(doorP.getX()-doorW/2, min(p1.getY(), p2.getY())), Point(doorP.getX()+doorW/2, doorP.getY()))
	door.draw(win)

	# Window
	t2.setText("Click to place a window...")
	windowP = win.getMouse() # Center of square
	while windowP.getX() > max(p1.getX(), p2.getX()) or \
		windowP.getX() < min(p1.getX(), p2.getX()) or \
		windowP.getY() < min(p1.getY(), p2.getY()) or \
		windowP.getY() > max(p1.getY(), p2.getY()):
		t2.setText("The window should be inside the house...")
		windowP = win.getMouse()

	windowW = doorW/2 # Window width
	window = Rectangle(Point(windowP.getX()-windowW/2,windowP.getY()-windowW/2), Point(windowP.getX()+windowW/2,windowP.getY()+windowW/2))
	window.draw(win)

	# Peak of the roof
	t2.setText("Click one more time to set the peak of the roof...")
	roofP = win.getMouse()
	while roofP.getX() > max(p1.getX(), p2.getX()) or \
		roofP.getX() < min(p1.getX(), p2.getX()) or \
		roofP.getY() < max(p1.getY(), p2.getY()):
		t2.setText("The roof should be above and within the limits of the house...")
		roofP = win.getMouse()

	l1 = Line(roofP, Point(p1.getX(), max(p1.getY(), p2.getY())))
	l1.draw(win)
	l2 = Line(roofP, Point(p2.getX(), max(p1.getY(), p2.getY())))	
	l2.draw(win)

	t2.setText("Looks good! (I think)")

	t3 = Text(Point(0, -9), "Click again to exit")
	t3.draw(win)
	win.getMouse()
	win.close()

if __name__ == '__main__':
	main()