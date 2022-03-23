from random import random

def main():
	printIntro()
	probAserve, probBserve, nSets = getInputs()
	winsA, winsB = simMatch(probAserve, probBserve, nSets)
	printSummary(winsA, winsB)

def printIntro():
	print('This is a simulation for the game of tennis.')
	print('')

def getInputs():
	probAserve = float(input("Probability that A wins one point while serving: "))
	probBserve = float(input("Probability that B wins one point while serving: "))
	nSets = int(input("How many sets to play? (generally 3 or 5): "))

	return probAserve, probBserve, nSets

def simMatch(probAserve, probBserve, nSets):
	setsA = setsB = 0
	counter = 1
	# Best of nSets
	while setsA < nSets and setsB < nSets:
		print('\nSet {} is starting'.format(counter))
		winner = simSet(probAserve, probBserve)
		print('Set {} won by {}'.format(counter, winner))
		if winner == 'A':
			setsA += 1
		else:
			setsB += 1

		counter += 1

	return setsA, setsB

def simSet(probAserve, probBserve):
	winsA = winsB = 0
	serving = 'A'
	while winsA < 6 and winsB < 6:
		winner = simGame(probAserve, probBserve, serving)
		
		if winner == 'A':
			winsA += 1
		else:
			winsB += 1

		print('Player {} served the game, and player {} won the game (A:{}-B:{})'.format(serving, winner, winsA, winsB))

		if serving == 'A':
			serving = 'B'
		else:
			serving = 'A'

	# If score is 6 to 4, or 6 to 3, etc, set is done
	if (winsA == 6 or winsB == 6) and abs(winsA-winsB) >= 2:
		if winsA > winsB:
			return 'A'
		else:
			return 'B'

	# If score is 6 to 5, play one more game
	if abs(winsA-winsB) == 1:
		winner = simGame(probAserve, probBserve, serving)
		if winner == 'A':
			winsA += 1
		else:
			winsB += 1

		print('Player {} served the game, and player {} won the game (A:{}-B:{})'.format(serving, winner, winsA, winsB))			

	# If score is 7 to 5, one player won the set
	if abs(winsA-winsB) == 2:
		if winsA > winsB:
			return 'A'
		else:
			return 'B'

	# If score is 6 to 6, tiebreak
	print('Tiebreak starting...')
	winsAtiebreak = winsBtiebreak = 0
	while not gameOverTieBreak(winsAtiebreak, winsBtiebreak):
		winner = simGame(probAserve, probBserve, serving)
		if winner == 'A':
			winsAtiebreak += 1
		else:
			winsBtiebreak += 1

		print('+ Player {} served the game, and player {} won the game (A:{}-B:{})'.format(serving, winner, winsAtiebreak, winsBtiebreak))



	if winsAtiebreak > winsBtiebreak:
		winsA += 1
	else:
		winsB += 1

	print('Player {} served the game, and player {} won the game (A:{}-B:{})'.format(serving, winner, winsA, winsB))		

	if winsA > winsB:
		return 'A'
	else:
		return 'B'


def simGame(probAserve, probBserve, serving):
	winsA = winsB = 0

	while not gameOverRegularGame(winsA, winsB):
		if serving == 'A':
			if random() < probAserve:
				winsA += 1
			else:
				winsB += 1

		else:
			if random() < probBserve:
				winsB += 1
			else:
				winsA += 1

	if winsA > winsB:
		return 'A'
	else:
		return 'B'

def gameOverRegularGame(winsA, winsB):
	return (winsA > 3 or winsB > 3) and abs(winsA-winsB) >= 2

def gameOverTieBreak(winsA, winsB):
	return (winsA >= 7 or winsB >= 7) and abs(winsA-winsB) >= 2

def printSummary(winsA, winsB):
	print('\nGame over!')
	if winsA > winsB:
		print('Player A won the match! {} to {}'.format(winsA, winsB))
	else:
		print('Player B won the match! {} to {}'.format(winsB, winsA))


if __name__ == '__main__':
	main()