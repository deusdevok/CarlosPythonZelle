def main():
	try:
		year = int(input('Enter a year (integer between 1982 and 2048): '))
	except ValueError:
		print('Invalid input.')

	if year < 1982 or year > 2048:
		print('Year must be a number between 1982 and 2048.')
		return

	a = year%19
	b = year%4
	c = year%7
	d = (19*a + 24)%30
	e = (2*b + 4*c + 6*d + 5)%7

	day = 22 + d + e

	if day <= 31:
		print('The date is March {}'.format(day))
	else:
		print('The date is April {}'.format(day - 31))

if __name__ == '__main__':
	main()