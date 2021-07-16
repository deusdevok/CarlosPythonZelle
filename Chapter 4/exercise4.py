# Winter scene with a Christmas tree
# and a snowman
# Using this website to pick RGB colors:
# https://www.rapidtables.com/web/color/RGB_Color.html

from graphics import *

def main():
	win = GraphWin("Winter", 640, 640)
	win.setCoords(0, 0, 100, 100)
	win.setBackground(color_rgb(189,238,246))

	treeBase = Rectangle(Point(20, 0), Point(30, 30))
	treeBase.setFill(color_rgb(196,101,7))

	treeGreen = Polygon(Point(15,30), Point(35,30), Point(25,70))
	treeGreen.setFill(color_rgb(31,134,15))

	snowmanLegs = Circle(Point(70, 20), 15)
	snowmanLegs.setWidth(3)
	snowmanLegs.setFill("white")

	snowmanTorso = Circle(Point(70, 40), 12)
	snowmanTorso.setWidth(3)
	snowmanTorso.setFill("white")

	snowmanHead = Circle(Point(70, 55), 8)
	snowmanHead.setWidth(3)
	snowmanHead.setFill("white")

	snowmanLeftEye = Circle(Point(67, 58), 1)
	snowmanLeftEye.setFill("black")

	snowmanRightEye = snowmanLeftEye.clone()
	snowmanRightEye.move(6, 0)

	snowmanNose = Polygon(Point(70,55), Point(69,52), Point(77, 52))
	snowmanNose.setFill(color_rgb(196,98,12))

	treeBase.draw(win)
	treeGreen.draw(win)

	snowmanLegs.draw(win)
	snowmanTorso.draw(win)
	snowmanHead.draw(win)

	snowmanLeftEye.draw(win)
	snowmanRightEye.draw(win)

	snowmanNose.draw(win)
	
	win.getMouse()
	win.close()
main()