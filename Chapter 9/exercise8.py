from random import choice

def main():
	printIntro()
	N = getInputs()
	p = simulateNGames(N)
	printSummary(N, p)

def printIntro():
	print('\nWelcome to the game of Blackjack!')
	print('\nGoal: draw cards that total as close to 21 points as possible without going over.')
	print('\nFace cards count as 10 points,')
	print('aces count as 1 or 11,')
	print('and all other cards count their numeric value.')

def getInputs():
	N = int(input('How many games you want to simulate (int): '))
	return N

def simulateNGames(N):
	busts = 0
	for _ in range(N):
		result = simulateOneGame()
		if not result:
			busts += 1

	return busts/N

def simulateOneGame():
	cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
	total = 0
	hasAce = False

	while total < 17:

		currentCard = choice(cards) # Take one card from the deck (at random)
		if currentCard in ['J', 'Q', 'K']:
			total += 10
		elif currentCard != 'A':
			total += currentCard
		else: # The card is an 'A' (ace)
			total += 1
			hasAce = True

		if hasAce and total+10 <= 21 and total+10 >= 17:
			total += 10

		#print('Card: {}; Total points: {}'.format(currentCard, total))

	if total > 21:
		#print('BUSTED!\n')
		result = False
	else:
		#print('Total points: {}\n'.format(total))
		result = True

	return result


def printSummary(N, p):
	print('\nGames played: {}'.format(N))
	print('Probability that the dealer will bust: {:.2%}'.format(p))

if __name__ == '__main__':
	main()