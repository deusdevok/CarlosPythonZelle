import math

def nextGuess(guess, x):
	return (guess + x/guess)/2

def main():
	x = float(input("Enter the value you want to calculate the square root of: "))
	n = int(input("How many guesses you want? "))
	guess = x/2
	for _ in range(n):
		guess = nextGuess(guess, x)

	print("The guess is:", guess)
	print("The difference with math.sqrt(x) is:", abs(guess - math.sqrt(x)))

main()