def main() :
	print("wc (word count) program")

	infileName = input("Enter the file name ")

	# Open the file
	infile = open(infileName, "r")
	chars = infile.read()
	infile.close()

	nLines = len(chars.split('\n'))
	nWords = len(chars.split())
	nChars = len(chars)

	print('\nlines, words and characters are, respectively:\n')
	print('{} {} {}'.format(nLines, nWords, nChars))

	


main()