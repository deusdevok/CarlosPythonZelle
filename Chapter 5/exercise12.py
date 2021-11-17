# futval . py
# A program to compute the value of an investment
# carried 10 years into the future
# Improved for exercise 12, chapter 5

def main() :
	print("This program calculates the future value")
	print("of a number of years investment.")

	principal = eval(input("Enter the initial principal: "))
	years = eval(input("Enter the number of years: "))
	rate = eval(input("Enter the annual interest rate (eg: 15% would be 0.15): "))

	print('Year   Value')
	print('--------------')
	for i in range(years+1):
		print('{0:3}   ${1:7.2f}'.format(i, principal))
		principal = principal * (1 + rate)

main()