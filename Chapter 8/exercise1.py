def nFibo(n):
	# 1, 1, 2, 3, 5, 8, 13, ...
	a, b = 1, 1
	for _ in range(n-1):
		# One way is to use an auxiliary variable
		#aux = b
		#b = a + b
		#a = aux

		# Another way is to use multiple assignment (Python trick)
		a, b = b, a+b
	return a

def main():
	n = int(input('Enter a number n (nth Fibonacci number): '))
	print(nFibo(n))

if __name__ == '__main__':
	main()