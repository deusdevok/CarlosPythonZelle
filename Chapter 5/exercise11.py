# File: chaos.py
# A simple program illustrating chaotic vehavior.
# Improved (exercise 11 from chapter 5)

def main():
    print("This program illustrates a chaotic function\n")

    n1 = eval(input("Enter a number between 0 and 1 (n1): "))
    n2 = eval(input("Enter a number between 0 and 1 (n2): "))
    n = eval(input("How many numbers should I print? "))

    print()
    print('index     {}       {}'.format(n1, n2))
    print('---------------------------')
    for i in range(n):
        n1 = 3.9*n1*(1-n1)
        n2 = 3.9*n2*(1-n2)

        print('{:3} {:11.6f} {:11.6f}'.format(i+1, n1, n2))

main()
