# Numerology program

def main():
    name = input('Enter your name: ')
    text = name.lower()
    num = 0
    for ch in text:
    	num += ord(ch)-ord('a')+1
    print('The numeric value of {} is {}'.format(name, num))
main()
