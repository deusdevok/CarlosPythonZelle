import random

def main():
	printIntro()
	N = getInputs()
	wins = simNGames(N)
	printSummary(wins, N)

def printIntro():
	print('This is the game of "Craps"')
	print('A player rolls a pair of six-sided dice')

def getInputs():
	n = int(input('How many games you want to simulate (int)? '))
	return n

def simNGames(N):
	wins = 0
	for _ in range(N):
		win = simOneGame() # Returns True or False
		if win:
			wins += 1
	return wins

def simOneGame():
	dice1 = random.randrange(1, 6)
	dice2 = random.randrange(1, 6)
	total = dice1 + dice2

	if total in [2, 3, 12]:
		return False # False means lose

	if total in [7, 11]:
		return True # True means win

	# Roll for point
	while True:
		dice1 = random.randrange(1, 6)
		dice2 = random.randrange(1, 6)
		total2 = dice1 + dice2

		if total2 == 7:
			return False

		if total2 == total:
			return True	

def printSummary(wins, N):
	print('\nPlayer won {} out of {} games'.format(wins, N))
	print('Probability that player wins: {:.3f}'.format(wins/N))

if __name__ == '__main__':
	main()