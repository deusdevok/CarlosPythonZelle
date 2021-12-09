# Fibonacci
# 1 1 2 3 5 8 13 21

def fibo(n):
	a, b = 1, 1
	for _ in range(n-2):
		a, b = b, a+b
	return b

def main():
	print("Fibonacci sequence")
	n = int(input("Enter the desired nth Fibonacci number: "))
	print("The nth Fibonacci number is", fibo(n))
	
main()