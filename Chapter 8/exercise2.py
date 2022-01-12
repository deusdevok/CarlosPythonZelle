def main():
	print(r'V\T')
	print('='*20)
	V = 0
	while V <= 50:
		T = -20
		while T <= 60:
			# windchill index
			W = 35.74+0.6215*T-35.75*V**0.16+0.4275*T*V**0.16
			#print()
			T += 10
		V += 5

if __name__ == '__main__':
	main()