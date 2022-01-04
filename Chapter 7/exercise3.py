def main():
	try:
		score = int(input('Enter the score (0-100): '))
	except ValueError:
		print('Invalid input.')
		return

	if score > 100 or score < 0:
		print('The score must be an integer between 0 and 100.')
		return

	if score >= 90:
		grade = 'A'
	elif score >= 80:
		grade = 'B'
	elif score >= 70:
		grade = 'C'
	elif score >= 60:
		grade = 'D'
	else:
		grade = 'F'

	print('Your grade is {}'.format(grade))
	

if __name__ == '__main__':
	main()