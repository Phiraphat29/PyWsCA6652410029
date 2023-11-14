import math

def squareArea() :
    try :
        width = float(input("ป้อนความกว้างของสี่เหลี่ยม: "))
        length = float(input("ป้อนความยาวของสี่เหลี่ยม: "))
        result = width * length
        print("%.2f" % result)
    except ValueError :
        print("ป้อนตัวเลข")
        squareArea()

def circleArea() :
    try :
        radius = float(input("ป้อนรัศมีวงกลม: "))
        result = math.pi * radius ** 2
        print("%.2f" % result)
    except ValueError :
        print("ป้อนตัวเลข")
        circleArea()
