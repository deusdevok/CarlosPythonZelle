# Sum of the first cubes n natural numbers
def main():
	print("This program computes the sum of the cubes of the first n natural numbers\n")
	n = int(input("Enter a natural number: "))
	res = 0
	for i in range(1, n+1):
		res += i**3
	print("The sum from 1 to ", n, "^3 is ", res, sep='')
main()