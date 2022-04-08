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
	distance = 0
	for _ in range(k):
		x, y = 0, 0
		for _ in range(n):
			direction = choice(['F', 'B', 'L', 'R']) # Forward, Backward, Left or Right
			if direction == 'F':
				y += 1
			elif direction == 'B':
				y -= 1
			elif direction == 'L':
				x -= 1
			else:
				x += 1

		distance += (x**2 + y**2)**0.5

	return distance/k

def printSummary(steps):
	print('\nAverage distance away from the starting point: {}'.format(steps))


if __name__ == '__main__':
	main()