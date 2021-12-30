def main():
	try:
		score = int(input('Enter the score (0-5): '))
	except ValueError:
		print('Your input is invalid.')
		return

	if score == 5:
		grade = 'A'
	elif score == 4:
		grade = 'B'
	elif score == 3:
		grade = 'C'
	elif score == 2:
		grade = 'D'
	elif score == 1 or score == 0:
		grade = 'F'
	else:
		print('You entered an invalid score. Please enter an integer number between 0 and 5.')
		return

	print('Your grade is {}'.format(grade))

if __name__ == '__main__':
	main()