# Goldbach conjecture

import math

def main():

	def isprime(n):
		d = 2
		while d <= math.sqrt(n):
			if n%d == 0:
				return False
			d += 1

		return True

	print('Goldbach conjecture:')
	print('"Every even number is the sum of two prime numbers"\n')

	try:
		n = int(input('Enter an even number greater than 2: '))
	except ValueError:
		print('Invalid input. It must be an integer.')
		return

	if n%2 != 0 or n <= 2:
		print('You entered an odd number or a number less than 3. Aborting.')
		return

	for d1 in range(2, n):
		for d2 in range(d1, n):
			if isprime(d1) and isprime(d2) and d1+d2 == n:
				print('{} = {} + {}'.format(n, d1, d2))
				#return

if __name__ == '__main__':
	main()