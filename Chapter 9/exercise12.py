from random import choice

def main():
	printIntro()
	n, k = getInputs()
	stepsAverage = randomWalk(n, k)
	printSummary(stepsAverage)

def printIntro():
	print('This program simulates a Random Walk.')
	print('You will be asked how many steps to simulate.')

def getInputs():
	n = int(input('How many steps you want for the Random Walk (int)? '))
	k = int(input('How many times you want to simulate to make an average (int)? '))
	return n, k

def randomWalk(n, k):
	stepsTotal = 0
	for _ in range(k):
		steps = 0
		for _ in range(n):
			coin = choice(['H', 'T']) # Heads or Tails
			if coin == 'H':
				steps += 1
			else:
				steps -= 1
		stepsTotal += abs(steps)

	return (stepsTotal)/k

def printSummary(steps):
	print('\nAverage number of steps away from the starting point: {}'.format(steps))


if __name__ == '__main__':
	main()