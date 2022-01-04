def main():
	try:
		weight = float(input('Enter the weight in pounds (float): '))
		height = float(input('Enter the height in inches (float): '))
		# Example weight: 154 pounds
		# Example height: 67 inches
	except ValueError:
		print('Invalid input.')
		return

	if weight <= 0 or height <= 0:
		print('Inputs must be positive numbers.')
		return

	BMI = weight*720/height**2
	print('Your BMI is: {}'.format(BMI))

	if BMI >= 19 and BMI <= 25:
		print('You are within the healthy range. Good job!')
	elif BMI < 19:
		print('You are below the healthy range.')
	else:
		print('You are above the healthy range.')

if __name__ == '__main__':
	main()