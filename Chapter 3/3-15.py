import math

def main():
	print("This program approximates the value of pi using a sum of terms\n")
	n = int(input("How many terms do you want to consider (enter an integer value)? "))
	total = 0
	sgn = 1
	for i in range(1, 2*n, 2):
		total += sgn*4/i
		sgn = -sgn

	print("Computed value for pi:", total)
	print("Difference between this value and math.pi:", abs(math.pi - total))
main()