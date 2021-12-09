def sumN(n):
	s = 0
	for i in range(1, n+1):
		s += i
	return s

def sumNCubes(n):
	s = 0
	for i in range(1, n+1):
		s += i**3
	return s

n = int(input('Enter a natural number: '))

print('Sum of the first {} natural numbers: {}'.format(n, sumN(n)))

print('Sum of the cubes of the first {} natural numbers: {}'.format(n, sumNCubes(n)))