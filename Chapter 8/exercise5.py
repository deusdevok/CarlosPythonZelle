# Determines if n is prime.

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

	d = 2
	while d <= math.sqrt(n):
		if n%d == 0:
			print('{} is not prime'.format(n))
			return
		d += 1

	print('{} is prime!'.format(n))

if __name__ == '__main__':
	main()