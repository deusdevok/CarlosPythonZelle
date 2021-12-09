import math

def sphereArea(radius):
	return 4*math.pi*radius**2

def sphereVolume(radius):
	return (4/3)*math.pi*radius**3

r = 1

V = sphereVolume(r)
A = sphereArea(r)

print('Volume = ', V)
print('Surface = ', A)