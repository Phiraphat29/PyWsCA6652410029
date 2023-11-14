import math

def squareCube():
    try :
        width = float(input("ป้อนความกว้างของสี่เหลี่ยม: "))
        length = float(input("ป้อนความยาวของสี่เหลี่ยม: "))
        height = float(input("ป้อนความสูงของสี่เหลี่ย: "))
        result = width * length * height
        print("%.2f" % result)
    except ValueError :
        print("ป้อนตัวเลข")
        squareCube()


def circleCube():
    try :
        radius = float(input("ป้อนรัศมีวงกลม: "))
        result = 4/3 * math.pi * radius ** 3
        print("%.2f" % result)
    except ValueError :
        print("ป้อนตัวเลข")
        circleCube()
