from graphics import *

def main() :

	win = GraphWin("Five-click House", 640, 640)
	win.setBackground("white")
	win.setCoords(-10, -10, 10, 10)

	t1 = Text(Point(0, 9), "Click five times to draw a house :)")
	t1.draw(win)
	t2 = Text(Point(0, 8), "Let's start with the frame of the house. Click somewhere...")
	t2.draw(win)

	# Rectangular frame of the house
	p1 = win.getMouse()
	t2.setText("Click one more time to draw the frame...")
	p2 = win.getMouse()
	rect = Rectangle(p1, p2)
	rect.draw(win)

	# Door
	t2.setText("Click inside to draw a door (top edge)...")
	doorP = win.getMouse() # Center of the top edge of the door
	doorW = abs(p1.getX()-p2.getX())/5 # Door width
	door = Rectangle(Point(doorP.getX()-doorW/2, min(p1.getY(), p2.getY())), Point(doorP.getX()+doorW/2, doorP.getY()))
	door.draw(win)

	# Window
	t2.setText("Click to place a window...")
	windowP = win.getMouse() # Center of square
	windowW = doorW/2 # Window width
	window = Rectangle(Point(windowP.getX()-windowW/2,windowP.getY()-windowW/2), Point(windowP.getX()+windowW/2,windowP.getY()+windowW/2))
	window.draw(win)

	# Peak of the roof
	t2.setText("Click one more time to set the peak of the roof...")
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
	
main()