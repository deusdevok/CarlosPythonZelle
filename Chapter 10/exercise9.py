import numpy as np

class Sphere:
    
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def surfaceArea(self):
        return 4*np.pi*self.radius**2

    def volume(self):
        return (4/3)*np.pi*self.radius**3

def main():
    r = float(input('Enter the radius of the sphere (float): '))
    s = Sphere(r)
    print('Area: {}\nVolume: {}'.format(s.surfaceArea(), s.volume()))

if __name__ == '__main__':
    main()