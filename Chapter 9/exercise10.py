from random import random

def main():
	printIntro()
	n = getInputs()
	pi = computePi(n)
	printSummary(pi)

def printIntro():
	print('This program computes the value of pi')
	print('using Monte Carlo techniques.')

def getInputs():
	n = int(input('\nHow many darts you want to simulate (int): '))
	return n

def computePi(n):
	# Number of points that lie inside the circle
	h = 0

	for _ in range(n):
		# Generate random x and y between -1 and 1
		x = 2*random() - 1
		y = 2*random() - 1
		if x**2 + y**2 <= 1:
			h += 1

	return 4*h/n

def printSummary(pi):
	print('\nThe value of pi is {}\n'.format(pi))

if __name__ == '__main__':
	main()