# Caesar cipher

def main():
	text = input('Enter the text to encode: ')
	key = int(input('Enter the key (integer): '))
	o = ''
	for ch in text:
		o += chr(ord(ch)+key)
	print(o)
main()