def main():
	HDD = 0 # Heating Degree Days
	CDD = 0 # Cooling Degree Days

	while True:
		d = input('Enter the average temperature '
			'of the day (empty to finish): ')

		if d == '':
			break

		d = float(d)

		if d < 60:
			HDD += 60-d
		elif d > 80:
			CDD += d-80

	print('HDD: {:.2f}'.format(HDD))
	print('CDD: {:.2f}'.format(CDD))

if __name__ == '__main__':
	main()