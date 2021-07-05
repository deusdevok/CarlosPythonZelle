import math
def main():
	print("Enter the lengths of the triangle:\n")
	a = float(input("a: "))
	b = float(input("b: "))
	c = float(input("c: "))

	# Heron's formula
	s = (a+b+c)/2
	A = math.sqrt(s*(s-a)*(s-b)*(s-c))
	print("Area = ", A)

main()