def squareEach(nums):
	# Modifies the list by squaring each entry
	# nums: list of numbers
	for i in range(len(nums)):
		nums[i] = nums[i]**2
	return nums

def sumList(nums):
	# Returns the sum of the numbers in the list
	# nums: list of numbers
	return sum(nums)

def toNumbers(strList):
	# Modifies each entry in the list
	# by converting it to a number.
	# strList: list of strings, each represents a number
	for i in range(len(strList)):
		strList[i] = int(strList[i])
	return strList

def main():
	fileName = input('Enter the file name: ')
	f = open(fileName, 'r')
	nums = f.read().splitlines()
	f.close()
	print('List: ', nums)
	res = sumList(squareEach(toNumbers(nums)))
	
	print('Sum of the squares of the numbers: ', res)

main()