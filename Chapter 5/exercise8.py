# Caesar cipher
# Circular

def main():
	text = input('Enter the text to encode: ')
	key = int(input('Enter the key (integer): '))
	alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz'
	
	o = ''
	for ch in text:
		pos = alp.find(ch) # gives the index in alp where ch is present
		newpos = (pos+key)%len(alp) # circularly compute the new pos
		o += alp[newpos]
	print(o)
main()