# futval_graph.py (modified so the inputs are in the GUI)
# A program to compute the value of an investment
# carried 10 years into the future

from graphics import *

def main() :
	#print("This program calculates the future value")
	#print("of a number of years investment.")
	#print("It gives a bar plot of each year value.")

	# Create a graphics window with labels on left edge
	win = GraphWin("Investment Growth Chart", 640, 480)
	win.setBackground("white")
	win.setCoords(-1.75, -200, 11.5, 10400)

	t1 = Text(Point((-1.75+11.5)/2, 8000), "Welcome to this")
	t2 = Text(Point((-1.75+11.5)/2, 7000), "Enter the values")
	t3 = Text(Point((-1.75+11.5)/2, 3000), "Click anywhere to continue")

	# Ask user input on screen
	t4 = Text(Point(1,5000), "       Initial Principal:")
	t5 = Text(Point(1,4000), "Annualized Interest Rate:")

	t1.draw(win)
	t2.draw(win)
	t3.draw(win)
	t4.draw(win)
	t5.draw(win)

	inputPrincipal = Entry(Point(4, 5000), 7)
	inputPrincipal.setText("2000.0")
	inputPrincipal.draw(win)

	inputAPR = Entry(Point(4, 4000), 7)
	inputAPR.setText("0.10")
	inputAPR.draw(win)

	win.getMouse()

	# Undraw text
	t1.undraw()
	t2.undraw()
	t3.undraw()
	t4.undraw()
	t5.undraw()
	inputPrincipal.undraw()
	inputAPR.undraw()

	# Go to next screen
	Text(Point(-1, 0), ' 0.0K').draw(win)
	Text(Point(-1, 2500), ' 2.5K').draw(win)
	Text(Point(-1, 5000), ' 5.0K').draw(win)
	Text(Point(-1, 7500), ' 7.5K').draw(win)
	Text(Point(-1, 10000), ' 10.0K').draw(win)

	principal = float(inputPrincipal.getText())
	apr = float(inputAPR.getText())

	# Draw bar for initial principal
	bar = Rectangle(Point(0, 0), Point(1, principal))
	bar.setFill("green")
	bar.setWidth(2)
	bar.draw(win)

	# Draw bars for successive years
	for year in range(1, 11):
		# calculate value for the next year
		principal = principal * (1 + apr)
		# draw bar for this value
		bar = Rectangle(Point(year, 0), Point(year+1, principal))
		bar.setFill("green")
		bar.setWidth(2)
		bar.draw(win)

	
	win.getMouse()
	win.close()
	
main()