from graphics import *
import math

def drawFace(center, size, win):
	# size is the radius of the face (an int)

	bigCircle = Circle(center, size)
	bigCircle.setFill("yellow")
	bigCircle.draw(win)

	r = size/1.8
	mouthDown = Circle(center, r)
	mouthDown.setWidth(size/20)
	mouthDown.setOutline("red")
	mouthDown.draw(win)
	
	cX = center.getX()
	cY = center.getY()

	mouthUp = Polygon(Point(cX-r, cY), Point(cX-r, cY+r), 
		Point(cX+r, cY+r), Point(cX+r, cY))
	mouthUp.setFill("yellow")
	mouthUp.setOutline("yellow")
	mouthUp.setWidth(size/20)
	mouthUp.draw(win)

	leftEye = Circle(Point(cX-r/1.5, cY+r/1.5), size/10)
	leftEye.setFill("blue")
	leftEye.draw(win)

	rightEye = leftEye.clone()
	rightEye.move(2*r/1.5, 0)
	rightEye.draw(win)
	

def main():
	fileName = input('Enter the name of the file (e.g.: ex16test.png): ')

	nFaces = int(input('How many faces you want to block (int)? '))

	myImg = Image(Point(0, 0), fileName)
	print(myImg.getWidth(), myImg.getHeight())

	win = GraphWin("Photo Anonymizer", myImg.getWidth(), myImg.getHeight())
	
	win.setCoords(-myImg.getWidth(), -myImg.getHeight(), myImg.getWidth(), myImg.getHeight())
	
	myImg.draw(win)

	for _ in range(nFaces):
		pCenter = win.getMouse()
		pSize = win.getMouse()
		size = math.sqrt((pCenter.getX()-pSize.getX())**2+(pCenter.getY()-pSize.getY())**2)
		drawFace(pCenter, size, win)

	win.getMouse()
	win.close()
main()