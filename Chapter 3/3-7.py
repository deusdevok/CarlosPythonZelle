import math

def main():
	print("This program computes the distance between two points in the (x,y) plane")
	x1 = float(input("x1 = "))
	y1 = float(input("y1 = "))
	x2 = float(input("x2 = "))
	y2 = float(input("y2 = "))
	distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
	print("Distance = ", distance)

main()