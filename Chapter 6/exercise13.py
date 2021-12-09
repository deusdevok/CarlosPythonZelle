def toNumbers(strList):
	# Modifies each entry in the list
	# by converting it to a number.
	# strList: list of strings, each represents a number
	for i in range(len(strList)):
		strList[i] = int(strList[i])
	return strList

def main():
	strList = ['1', '2', '3']
	print(toNumbers(strList))

main()