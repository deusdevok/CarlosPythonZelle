# Acronym program

def main():
    text = input('Enter your phrase (eg: "random access memory"): ')
    acronym = ''
    for t in text.split():
    	acronym += t[0].upper()
    print('The acronym is:', acronym)
main()
