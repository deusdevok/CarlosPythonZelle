def main():

	HDD = 0 # Heating Degree Days
	CDD = 0 # Cooling Degree Days

	fileName = input('Enter the file name: ')
	infile = open(fileName, 'r')
	line = infile.readline() # Read first line


	while line != '':

		d = float(line)

		if d < 60:
			HDD += 60-d
		elif d > 80:
			CDD += d-80

		line = infile.readline()

	print('HDD: {:.2f}'.format(HDD))
	print('CDD: {:.2f}'.format(CDD))

if __name__ == '__main__':
	main()