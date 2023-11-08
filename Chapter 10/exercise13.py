from graphics import *
from button import Button

class Face:
    def __init__(self, window, center, size):
        eyeSize = 0.15*size
        eyeOff = size/3.0
        mouthSize = 0.8*size
        mouthOff = size/2.0

        self.center = center
        self.mouthSize = mouthSize
        self.mouthOff = mouthOff
        self.window = window
        self.size = size

        self.head = Circle(center, size)
        self.head.draw(window)
        self.leftEye = Circle(center, eyeSize)
        self.leftEye.move(-eyeOff, -eyeOff)
        self.rightEye = Circle(center, eyeSize)
        self.rightEye.move(eyeOff, -eyeOff)
        self.leftEye.draw(window)
        self.rightEye.draw(window)
        p1 = center.clone()
        p1.move(-mouthSize/2, mouthOff)
        p2 = center.clone()
        p2.move(mouthSize/2, mouthOff)
        self.mouth = Line(p1, p2)
        self.mouth.draw(window)

    def smile(self):
        self.mouth.undraw()
        p1 = self.center.clone()
        p1.move(-self.mouthSize/2, self.mouthOff)
        p2 = self.center.clone()
        p2.move(0, self.mouthOff*1.5)
        p3 = self.center.clone()
        p3.move(self.mouthSize/2, self.mouthOff)

        mouth = Polygon([p1,p2,p3])
        mouth.draw(self.window)

    def wink(self):
        self.leftEye.undraw()
        p1 = self.center.clone()
        p1.move(-self.size/5, -self.size/3)
        p2 = self.center.clone()
        p2.move(-self.size/2.5, -self.size/3)
        newLeftEye = Line(p1, p2)
        newLeftEye.draw(self.window)

    def frown(self):
        pass

    def flinch(self):
        pass

def main():
    win = GraphWin("Face", 800, 600)
    center = Point(400, 300)
    size = 100
    face = Face(win, center, size)

    smileBtn = Button(win, Point(50,500), 80, 30, "Smile")
    winkBtn = Button(win, Point(150,500), 80, 30, "Wink")
    frownBtn = Button(win, Point(250,500), 80, 30, "Frown")
    flinchBtn = Button(win, Point(350,500), 80, 30, "Flinch")
    quitBtn = Button(win, Point(550,500), 80, 30, "Quit")

    smileBtn.activate()
    winkBtn.activate()
    frownBtn.activate()
    flinchBtn.activate()
    quitBtn.activate()

    pt = win.getMouse()

    while not quitBtn.clicked(pt):
        if smileBtn.clicked(pt):
            face.smile()
        
        if winkBtn.clicked(pt):
            face.wink()
        
        if frownBtn.clicked(pt):
            face.frown()

        if flinchBtn.clicked(pt):
            face.flinch()

        pt = win.getMouse()

    win.close()

if __name__ == '__main__':
    main()