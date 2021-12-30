def main():
	n = float(input('Enter the number of hours worked: '))
	hr = float(input('Enter the hourly rate: '))

	if n <= 40:
		wages = n*hr
	else:
		wages = 40*hr + (n-40)*1.5*hr

	print('Total wages for the week: {:.2f}'.format(wages))

if __name__ == '__main__':
	main()