# Sum of the first n natural numbers
def main():
	print("This program computes the sum of the first n natural numbers\n")
	n = int(input("Enter a natural number: "))
	res = 0
	for i in range(1, n+1):
		res += i
	print("The sum from 1 to", n, "is ", res)
main()