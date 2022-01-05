def main():

	date = input('Enter a date (MM/DD/YYYY): ')
	m, d, y = map(int, date.split('/'))

	if y%4 == 0:
		if y%100 == 0 and y%400 != 0:
			leap = False
		else:
			leap = True
	else:
		leap = False

	if m in [1, 3, 5, 7, 8, 10, 12]:
		maxDays = 31
	else:
		if m != 2:
			maxDays = 30
		else:
			if leap:
				maxDays = 29
			else:
				maxDays = 28

	if d > maxDays or m > 12:
		print('Invalid Date')
	else:
		print('Valid Date')

if __name__ == '__main__':
	main()