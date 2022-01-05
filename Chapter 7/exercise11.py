def main():
	try:
		year = int(input('Enter a year: '))
	except ValueError:
		print('Invalid input.')

	if year%4 == 0:
		if year%100 == 0 and year%400 != 0:
			print('No Leap year!')
		else:
			print('Leap year!')
	else:
		print('Not a leap year :(')

if __name__ == '__main__':
	main()