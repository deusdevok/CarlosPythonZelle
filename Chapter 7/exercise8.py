def main():
	age = int(input('Enter the age (integer): '))
	years = int(input('Enter the years of citizenship (integer): '))

	if age >= 30 and years >= 9:
		print('Eligible for U.S. Senate.')
	elif age >= 25 and years >= 7:
		print('Eligible for U.S. Representative.')
	else:
		print('Not eligible yet.')


if __name__ == '__main__':
	main()