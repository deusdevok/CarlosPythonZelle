import math

def areaPizza(r):
	return math.pi*r**2

def costPerSquareInch(p, A):
	return p/A

d = 15.92 # Diameter
p = 105.50 # Price (total)
r = d/2
A = areaPizza(r)

cost = costPerSquareInch(p, A) # Cost per square inch
print(cost)