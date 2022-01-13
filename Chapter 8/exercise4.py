# Syracuse (or Collatz or Hailstone) sequence

def main():
	x = int(input('Enter an integer number: '))
	print('The Syracuse sequence is:')
	while x != 1:
		print(int(x), end=', ')
		if x%2 == 0: # If x is even
			x = x/2
		else: # If x is odd
			x = 3*x + 1

	print(int(x))

if __name__ == '__main__':
	main()