# Numerology program
# Names can be multiple words

def main():
    name = input('Enter your name: ')
    text = name.lower()
    text = ''.join(text.split())
    num = 0

    for ch in text:
    	num += ord(ch)-ord('a')+1
    	
    print('The numeric value of {} is {}'.format(name, num))
main()
