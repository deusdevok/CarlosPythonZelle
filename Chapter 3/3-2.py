import math

d = 15.92 # Diameter
p = 105.50 # Price (total)
r = d/2
A = math.pi*r**2

cost = p/A # Cost per square inch
print(cost)