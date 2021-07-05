import math

def main():
	height = float(input("Height: "))
	degrees = float(input("Angle (degrees): "))

	radians = (math.pi/180)*degrees

	length = height/math.sin(radians)

	print("Length of the ladder: ", length)

main()