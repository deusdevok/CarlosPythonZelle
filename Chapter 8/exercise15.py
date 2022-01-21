# Converts a color image to its color negative
from graphics import *

def main():
	nameFile = input('Enter the name of the image: ')

	win = GraphWin('Image To color negative', 800, 800)

	myImage = Image(Point(400, 400), nameFile)

	nCols = myImage.getWidth()
	nRows = myImage.getHeight()

	myImage.draw(win)

	for row in range(nRows):
		for col in range(nCols):
			r, g, b = myImage.getPixel(col, row)
			myImage.setPixel(col, row, color_rgb(255-r, 255-g, 255-b))
		update()


	nameSaveFile = input('Enter the name of the saved color negative image: ')
	myImage.save(nameSaveFile)

	win.getMouse()
	win.close()

if __name__ == '__main__':
	main()