def main():
	try:
		credits = int(input('Enter the number of credits (more than or equal to 0): '))
	except ValueError:
		print('Invalid input.')
		return

	if credits < 0:
		print('The number of credits must be an integer greater than or equal to 0.')
		return

	if credits < 7:
		classStanding = 'Freshman'
	elif credits < 16:
		classStanding = 'Sophomore'
	elif credits < 26:
		classStanding = 'Junior'
	else:
		classStanding = 'Senior'

	print('Your class standing is {}'.format(classStanding))
	

if __name__ == '__main__':
	main()