# Average word length

def main():
	text = input('Enter the text: ')
	words = text.split()

	l = 0
	for word in words:
		l += len(word)
	print('The average length is {:.2f}'.format(l/len(words)))
	
main()