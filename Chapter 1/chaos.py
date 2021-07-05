# File: chaos.py
# A simple program illustrating chaotic vehavior.

def main(n1, n2):
    print("This program illustrates a chaotic function")
    #x = eval(input("Enter a number between 0 and 1: "))
    
    n = eval(input("How many numbers should I print? "))
    print("input ", n1, n2)
    for i in range(n):
        n1 = 3.9*n1*(1-n1)
        n2 = 3.9*n2*(1-n2)
        #x = 3.9*x*(1-x)
        #x = 3.9*(x-x*x)
        #x = 3.9*x-3.9*x*x
        #print(x)
        print(n1, n2)

main(0.15, 0.16)
