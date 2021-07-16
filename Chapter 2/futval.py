# futval . py
# A program to compute the value of an investment
# carried 10 years into the future
def main() :
	print("This program calculates the future value")
	print("of a number of years investment.")

	principal = eval(input("Enter the initial principal: "))
	years = eval(input("Enter the number of years: "))
	rate = eval(input("Enter the annual interest rate (eg: 15% would be 0.15): "))
	periods = eval(input("Number of times the interest is compounded each year: "))

	print('years   value')
	for i in range(years*periods):
		print('  {}   ${:.2f}'.format(i, principal))
		principal = principal * (1 + rate/periods)
	
	print('  {}   ${:.2f}'.format(i+1, principal))
	print()
	print("The value in", years, "years is: ", principal)
main()