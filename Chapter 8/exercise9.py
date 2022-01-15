def main():
	data = []
	while True:
		# Get inputs separated by a space
		d = input("Enter odometer reading (miles)\n"
			"and amount of gas used (galons)\n"
			"separated by a space\n"
			"(hit Enter to finish): ")

		# If input is blank, exit the while loop
		if d == '':
			break

		try:
			miles, galons = d.split(' ')
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

	totalMiles = sum([d[0] for d in data])
	totalGalons = sum([d[1] for d in data])

	print('Total MPG: {:.2f}'.format(totalMiles/totalGalons))



if __name__ == '__main__':
	main()