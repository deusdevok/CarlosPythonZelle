# Finds every prime number less than or equal to n.

import math

def main():
	try:
		n = int(input('Enter a positive whole number greater than 2: '))
	except ValueError:
		print('n must be positive integer...')
		return

	if n <= 2:
		print('The number must be greater than 2')
		return

	def isprime(n):
		d = 2
		while d <= math.sqrt(n):
			if n%d == 0:
				return False
			d += 1

		return True
	
	l = []
	for p in range(3, n+1):
		if isprime(p):
			l.append(p)

	print('List of prime numbers less than or equal to {}:'.format(n))
	print(l)

if __name__ == '__main__':
	main()