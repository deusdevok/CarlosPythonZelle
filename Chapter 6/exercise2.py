def antsMarch(number):
	return 'The ants go marching {} by {},'.format(number, number)

def hurrah():
	return ' hurrah! hurrah!'

def sing(number, rhyme):
	print(antsMarch(number) + hurrah())
	print(antsMarch(number) + hurrah())
	print(antsMarch(number))
	print('The little one stops to ' + rhyme + ',')
	print('And they all go marching down...')
	print('In the ground...')
	print('To get out...')
	print('Of the rain.')
	print('Boom! Boom! Boom!')

def main():
	numAndRhymes = {
		'one': 'suck his thumb', 
		'two': 'tie his shoe', 
		'three': 'cut his tree', 
		'four': 'get his loan', 
		'five': 'see his bride',
		'six': 'watch his six', 
		'seven': 'meet with Menem', 
		'eight': 'call his mate', 
		'nine': 'finish his line', 
		'ten': 'eat his cake'}

	for number in numAndRhymes:
		sing(number, numAndRhymes[number])

main()