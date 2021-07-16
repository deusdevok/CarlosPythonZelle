# futval . py
# A program to compute the value of an investment
# carried 10 years into the future

from graphics import *

def main() :
	print("This program calculates the future value")
	print("of a number of years investment.")
	print("It gives a bar plot of each year value.")

	principal = float(input("Enter the initial principal: "))
	apr = float(input("Enter the annualized interest rate: "))

	# Create a graphics window with labels on left edge
	win = GraphWin("Investment Growth Chart", 640, 480)
	win.setBackground("white")
	win.setCoords(-1.75, -200, 11.5, 10400)
	Text(Point(-1, 0), ' 0.0K').draw(win)
	Text(Point(-1, 2500), ' 2.5K').draw(win)
	Text(Point(-1, 5000), ' 5.0K').draw(win)
	Text(Point(-1, 7500), ' 7.5K').draw(win)
	Text(Point(-1, 10000), ' 10.0K').draw(win)

	# Draw bar for initial principal
	bar = Rectangle(Point(0, 0), Point(1, principal))
	bar.setFill("green")
	bar.setWidth(2)
	bar.draw(win)

	# Draw bars for successive years

	print('years   value')
	for year in range(1, 11):
		# calculate value for the next year
		principal = principal * (1 + apr)
		# draw bar for this value
		bar = Rectangle(Point(year, 0), Point(year+1, principal))
		bar.setFill("green")
		bar.setWidth(2)
		bar.draw(win)

	input("Press <Enter> to quit")
	win.close()
	
main()