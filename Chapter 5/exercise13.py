# futval . py
# A program to compute the value of an investment
# carried 10 years into the future
# Using batch mode

def main() :
	print("This program calculates the future value")
	print("of a number of years investment.")

	infileName = input("What file are the names in? ")
	outfileName = input("What file should the output go in? ")

	# Open the files
	infile = open(infileName, "r")
	outfile = open(outfileName, "w")

	for line in infile:
		principal, years, rate = line.split()

	principal, years, rate = float(principal), int(years), float(rate)

	print('Year   Value', file=outfile)
	print('--------------', file=outfile)
	for i in range(years+1):
		print('{0:3}   ${1:7.2f}'.format(i, principal), file=outfile)
		principal = principal * (1 + rate)

	infile.close()
	outfile.close()

	print('The table has been written to', outfileName)

main()