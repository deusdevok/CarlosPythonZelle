def main():
	# This exercise can be improved.
	# Should have a check for minutes to be under 60
	# A similar check for hours, should be below 24

	start = list(map(int, input('Starting time (HH:MM): ').split(':')))
	end = list(map(int, input('Ending time (HH:MM): ').split(':')))

	# We have two possible cases:
	# 1. 9:00 PM (21 hs) is between the starting and ending time
	# 2. starting and ending time is both below or above 9:00 PM

	if start[0] < 21 and end[0] >= 21:
		h1 = 21 - start[0]
		m1 = 0 - start[1]
		h2 = end[0] - 21
		m2 = end[1] - 0
		
		t1 = h1 + m1/60
		t2 = h2 + m2/60

		t = t1 + t2

		bill = 2.5*t1 + 1.75*t2
	else:
		h = end[0] - start[0]
		m = end[1] - start[1]
		
		t = h + m/60 # total time in hours
		
		if start[0] < 21:
			bill = 2.5*t
		else:
			bill = 1.75*t


	print('Total time: {} hours'.format(t))
	print('Total babysitting bill: ${}'.format(bill))
	#print('Expected babysitting bill: ${}\n'.format(expected))

if __name__ == '__main__':
	main()

	# Test cases:
	# The main function has to include parameters for the test cases to work:
	# def main(start, end, expected):

	'''
	# After 21
	s1 = [21, 00]
	s2 = [22, 00]
	e1 = 1.75 # expected result
	main(s1, s2, e1)

	s1 = [22, 00]
	s2 = [23, 30]
	e1 = 2.625 # expected result
	main(s1, s2, e1)

	# Before 21
	s1 = [19, 10]
	s2 = [20, 48]
	e1 = 4.08333 # expected result
	main(s1, s2, e1)

	# 21 in between
	s1 = [19, 15]
	s2 = [22, 20]
	e1 = 6.70833 # expected result
	main(s1, s2, e1)
	'''