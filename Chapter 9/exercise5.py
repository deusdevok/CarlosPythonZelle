from random import random

def main():
	printIntro()
	probA, probB, n = getInputs()
	winsAreg, winsBreg = simNGamesRegularVolley(n, probA, probB)
	winsArally, winsBrally = simNGamesRallyScoring(n, probA, probB)
	printSummary(winsAreg, winsBreg, winsArally, winsBrally, n)


def printIntro():
	print('This is a system that compares regular volleyball to those using rally scoring.')
	print('This will tell whether rally scoring magnifies, reduces or has')
	print('no effect on the relative advantage enjoyed by the better team.')

def getInputs():
	probA = float(input("What is the probability that team A wins one point (serve)? "))
	probB = float(input("What is the probability that team B wins one point (serve)? "))
	n = int(input("How many games to simulate? "))

	return probA, probB, n

def simNGamesRegularVolley(n, probA, probB):
	winsA = winsB = 0
	for i in range(n):
		A, B = playOneGameRegular(probA, probB)
		if A > B:
			winsA += 1
		else:
			winsB += 1

	return winsA, winsB

def simNGamesRallyScoring(n, probA, probB):
	winsA = winsB = 0
	for i in range(n):
		A, B = playOneGameRally(probA, probB)
		if A > B:
			winsA += 1
		else:
			winsB += 1

	return winsA, winsB

def playOneGameRegular(probA, probB):
	winsA = winsB = 0
	serving = 'A'

	while not gameOverRegular(winsA, winsB):
		if serving == 'A':
			if random() < probA:
				winsA += 1
			else:
				serving = 'B'
		else:
			if random() < probB:
				winsB += 1
			else:
				serving = 'A'

	return winsA, winsB		

def gameOverRegular(winsA, winsB):
	return (winsA >= 15 or winsB >= 15) and abs(winsA - winsB) >= 2	

def playOneGameRally(probA, probB):
	winsA = winsB = 0

	while not gameOverRally(winsA, winsB):
		if random() < probA:
			winsA += 1
		else:
			winsB += 1

	return winsA, winsB	

def gameOverRally(winsA, winsB):
	return (winsA >= 25 or winsB >= 25) and abs(winsA - winsB) >= 2	

def printSummary(winsAreg, winsBreg, winsArally, winsBrally, n):
	print('\nGames simulated: {}'.format(n))
	print('Regular volleyball:')
	print('Wins for A: {0} ({1:0.1%})'.format(winsAreg, winsAreg/n))
	print('Wins for B: {0} ({1:0.1%})'.format(winsBreg, winsBreg/n))

	print('\nUsing rally scoring:')
	print('Wins for A: {0} ({1:0.1%})'.format(winsArally, winsArally/n))
	print('Wins for B: {0} ({1:0.1%})'.format(winsBrally, winsBrally/n))

if __name__ == '__main__':
	main()