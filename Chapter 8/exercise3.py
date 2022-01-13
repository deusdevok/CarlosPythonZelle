def main():
	# Annualized interest rate
	AIR = 0.30 # 0.30 is 30% rate
	
	# Initial investment
	inv = 15
	finalOutcome = inv
	nYears = 0

	while finalOutcome < 2*inv:
		finalOutcome = (1+AIR)*finalOutcome
		nYears += 1

	print('The initial investment is doubled after {} years'.format(nYears))

if __name__ == '__main__':
	main()