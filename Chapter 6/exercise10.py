# Acronym program

def acronym(phrase):
    acron = ''
    for t in phrase.split():
    	acron += t[0].upper()
    return acron

def main():
    text = input('Enter your phrase (eg: "random access memory"): ')
    print('The acronym is:', acronym(text))
main()