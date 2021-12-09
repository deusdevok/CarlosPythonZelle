def squareEach(nums):
	# Modifies the list by squaring each entry
	# nums: list of numbers
	for i in range(len(nums)):
		nums[i] = nums[i]**2
	return nums

def main():
	nums = [1, 2, 3]
	print(squareEach(nums))

main()