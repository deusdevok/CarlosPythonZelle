from graphics import *
import math
from random import random

def main():
	n = int(input('How many steps (int)? '))
	win = GraphWin('Random Walk', 500, 500)
	win.setCoords(-50, -50, 50, 50) # xll, yll, xur, yur

	currP = Point(0, 0) # Initial point
	nextP = Point(0, 0)

	for _ in range(n):
		angle = random() * 2 * math.pi # angle in radians
		dx = math.cos(angle)
		dy = math.sin(angle)

		nextP.move(dx, dy)
		L = Line(currP, nextP)
		L.draw(win)

		currP.move(dx, dy)
		

	win.getMouse()
	win.close()

if __name__ == '__main__':
	main()