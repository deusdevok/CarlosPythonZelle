from random import random

def main():
	printIntro()
	probA, probB = getInputs()
	winsA, winsB = playOneGame(probA, probB)
	printSummary(winsA, winsB)

def printIntro():
	print('Welcome to the game of Volleyball!')
	print('Rally scoring: any team, serving or not, can score.')
	print('Games are played to 25, but must be won by at least two points.')

def getInputs():
	probA = float(input("What is the probability that team A wins one point (serve)? "))
	probB = float(input("What is the probability that team B wins one point (serve)? "))

	return probA, probB

def playOneGame(probA, probB):
	winsA = winsB = 0

	while not gameOver(winsA, winsB):
		if random() < probA:
			winsA += 1
		else:
			winsB += 1

	return winsA, winsB

def gameOver(winsA, winsB):
	return (winsA >= 25 or winsB >= 25) and abs(winsA - winsB) >= 2

def printSummary(winsA, winsB):
	if winsA > winsB:
		print('Team A won the game! {} to {}'.format(winsA, winsB))
	else:
		print('Team B won the game! {} to {}'.format(winsB, winsA))


if __name__ == '__main__':
	main()