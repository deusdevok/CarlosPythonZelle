# Greatest Common Divisor (GCD) using Euclid's algorithm.

def main():
	def GCD(n, m):
		while m != 0:
			# n%m finds the remainder of the division between n and m
			# % is the 'modulo' operator
			# https://docs.python.org/3.3/reference/expressions.html#binary-arithmetic-operations
			n, m = m, n%m
		return n

	n = int(input('Enter the first number: '))
	m = int(input('Enter the second number: '))
	
	print('GCD({}, {}) = {}'.format(n, m, GCD(n, m)))

if __name__ == '__main__':
	main()