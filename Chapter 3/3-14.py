def main():
	print("Computes the averages of the numbers you enter\n")
	n = int(input("How many numbers do you want to sum? "))
	print("\nNext, enter", n, "numbers")
	total = 0
	for i in range(n):
		print("\n", n-i, "numbers remaining...")
		m = float(input("Enter a number "))
		total += m
	print("\nThe average of your numbers is:", total/n)
main()