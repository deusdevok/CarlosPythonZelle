# Converts a color image to grayscale

from graphics import *

def main():
	nameFile = input('Enter the name of the image: ')

	win = GraphWin('Image To Grayscale', 800, 800)

	myImage = Image(Point(400, 400), nameFile)

	nCols = myImage.getWidth()
	nRows = myImage.getHeight()

	myImage.draw(win)

	for row in range(nRows):
		for col in range(nCols):
			r, g, b = myImage.getPixel(col, row)
			brightness = int(round(0.299*r + 0.587*g + 0.114*b))
			myImage.setPixel(col, row, color_rgb(brightness, brightness, brightness))
		myImage.undraw()
		myImage.draw(win)

	myImage.undraw()
	myImage.draw(win)

	nameSaveFile = input('Enter the name of the saved grayscale image: ')
	myImage.save(nameSaveFile)

	win.getMouse()
	win.close()

if __name__ == '__main__':
	main()