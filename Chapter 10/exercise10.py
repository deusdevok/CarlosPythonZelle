class Cube:

    def __init__(self, length):
        self.length = length

    def getLength(self):
        return self.length

    def surfaceArea(self):
        return 6*self.length**2

    def volume(self):
        return self.length**3

def main():
    length = float(input("Enter the cube's size length (float): "))
    myCube = Cube(length)
    print('Surface area: {}\nVolume: {}'.format(myCube.surfaceArea(), myCube.volume()))

if __name__ == '__main__':
    main()