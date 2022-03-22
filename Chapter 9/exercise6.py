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
	# Best of nSets
	while setsA < nSets and setsB < nSets:
		winner = simSet(probAserve, probBserve)
		if winner == 'A':
			setsA += 1
		else:
			setsB += 1

	return setsA, setsB

def simSet(probAserve, probBserve):
	winsA = winsB = 0
	serving = 'A'
	while winsA < 6 and winsB < 6 and abs(winsA-winsB) < 2:
		winner = simGame(probAserve, probBserve, serving)
		if winner == 'A':
			winsA += 1
		else:
			winsB += 1

	# If score is 6 to 4, or 6 to 3, etc, set is done
	if (winsA == 6 or winsB == 6) and abs(winsA-winsB) >= 2:
		return winsA, winsB

	# If score is 6 to 5, play one more game
	if abs(winsA-winsB) == 1:
		winner = simGame(probAserve, probBserve, serving)
		if winner == 'A':
			winsA += 1
		else:
			winsB += 1

	# If score is 7 to 5, one player won the set
	if abs(winsA-winsB) == 2:
		return winsA, winsB

	# If score is 6 to 6, tiebreak
	winsAtiebreak = winsBtiebreak = 0
	while winsAtiebreak < 7 and winsBtiebreak < 7 and abs(winsAtiebreak - winsBtiebreak) < 2:
		winner = simGame(probAserve, probBserve, serving)
		if winner == 'A':
			winsAtiebreak += 1
		else:
			winsBtiebreak += 1

	if winsAtiebreak > winsBtiebreak:
		winsA += 1
	else:
		winsB += 1

	return winsA, winsB

def simGame(probAserve, probBserve, serving):
	winsA = winsB = 0

	while not gameOver(winsA, winsB):
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

def gameOver(winsA, winsB):



if __name__ == '__main__':
	main()