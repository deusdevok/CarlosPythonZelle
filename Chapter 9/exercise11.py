from random import randint

def main():
	printIntro()
	n = getInputs()
	p = fiveOfAKind(n)
	printSummary(p)

def printIntro():
	print('This program computes the probability of rolling five')
	print('of a kind in a single roll of five six-sided dice.')

def getInputs():
	n = int(input('How many times you want to simulate the roll? '))
	return n

def fiveOfAKind(n):
	numberOfTrue = 0
	for _ in range(n):
		result = rollFiveDice() # True or False
		if result:
			numberOfTrue += 1

	return numberOfTrue/n


def rollFiveDice():
	dice = []
	for _ in range(5):
		dice.append(randint(1, 6))

	return len(set(dice)) == 1

def printSummary(p):
	print('Probability: {:.6f}'.format(p))

	pTheo = 6/6**5
	print('Theoretical probability: {:.6f}'.format(pTheo))

if __name__ == '__main__':
	main()