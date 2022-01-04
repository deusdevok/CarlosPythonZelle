def main():
	try:
		speedLimit = float(input('Speed limit (mph): '))
		clockedSpeed = float(input('Clocked speed (mph): '))
	except ValueError:
		print('Invalid input.')

	if speedLimit < 0 or clockedSpeed < 0:
		print("Inputs can't be negative.")
		return

	if clockedSpeed <= speedLimit:
		print('The speed was legal. No problem.')
		return
	elif clockedSpeed <= 90:
		fine = 50 + (clockedSpeed - speedLimit)*5
	else:
		fine = 250 + (clockedSpeed - speedLimit)*5

	print('You broke the law. You have to pay ${}.'.format(fine))

if __name__ == '__main__':
	main()