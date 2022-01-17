def main():
	data = []

	# Get inputs from a file
	fileName = input('Enter the name of the file: ')
	infile = open(fileName, 'r')
	line = infile.readline() # read first line

	while line != '': # do this while the file has a line
	
		# Separate each line by a space
		try:
			miles, galons = line.split(' ')
			miles, galons = float(miles), float(galons)
		except:
			print('Something went wrong.')
			return

		if miles < 0 or galons < 0:
			print("Inputs can't be negative numbers.")
			return

		MPG = miles/galons
		print('Current MPG: {:.2f}'.format(MPG))

		data.append([miles, galons])

		line = infile.readline() # read next line

	totalMiles = sum([d[0] for d in data])
	totalGalons = sum([d[1] for d in data])

	print('Total miles: {}'.format(totalMiles))
	print('Total galons: {}'.format(totalGalons))

	print('Total MPG: {:.2f}'.format(totalMiles/totalGalons))


if __name__ == '__main__':
	main()