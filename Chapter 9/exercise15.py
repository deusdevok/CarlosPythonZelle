'''
If the point is (0,0,0), the field of view is 1/6 on each face of the cube
Now the point is located at (0.5,0,0)
'''

from random import random


def main():
	x, n = getInputs()

	count = 0
	for _ in range(n):
		a, b, c = getRandomDirection()
		t = (1-x)/a
		if (-1 <= t*b <= 1) and (-1 <= t*c <= 1) and t > 0:
			count += 1

	print('\n{} out of {} points hit the front wall ({:.2%}%)'.format(count, n, count/n))
	print('FOV: {}'.format(count/n))


def getInputs():
	x = float(input('Position of the observer (float between -1 and 1): '))
	n = int(input('Number of points for the Monte Carlo simulation (int): '))
	return x, n

def getRandomDirection():
	# Generate random (x, y, z) between -1 and 1 inside the unit sphere
	while True:
		x = 2*random() - 1
		y = 2*random() - 1
		z = 2*random() - 1

		if x**2+y**2+z**2 < 1 and (x,y,z) != (0,0,0):
			return x, y, z
	


if __name__ == '__main__':
	main()