from PIL import Image
import os, sys

path = "D:\Carlos\Programas\Python\John Zelle Python Programming\Carlos Programs\Chapter 10\cardsImg\\"
dirs = os.listdir(path)

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((50,73), Image.ANTIALIAS)
            print(f)
            imResize.save(f + '.png', 'png', quality=90)

resize()