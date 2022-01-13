def main():
	print(''.center(86, '='))
	print(' Windchill Index '.center(86, '='))
	print(''.center(86, '='))
	print()

	print(r'V[mph]\T[°F] | ', end='')
	T = -20
	while T <= 60:
		print('{:.0f}'.format(T).rjust(6), end='\t')
		T += 10

	print()
	print(''.center(86, '-'))
	V = 0
	while V <= 50:
		T = -20
		print('{:.0f}'.format(V).rjust(12), end=' | ')
		while T <= 60:
			# windchill index
			W = 35.74+0.6215*T-35.75*V**0.16+0.4275*T*V**0.16
			print('{:.2f}'.format(W).rjust(6), end='\t')
			T += 10
		print()
		V += 5

if __name__ == '__main__':
	main()