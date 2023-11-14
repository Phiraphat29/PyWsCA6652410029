import area
import cube

try :
    print("************************************************ AREA &CUBE ************************************************")
    print("1. พื้นที่สี่เหลี่ยม \n2. พื้นที่วงกลม \n3. ปริมาตรทรงสี่เหลี่ยม \n4. ปริมาตรทรงกลม \n0. ออกจากการทํางาน")

    def selection():
        modeSelect = input('โปรดป้อนตัวเลขที่คุณต้องการหาค่า : ')
        if modeSelect == "1" :
            area.squareArea()
        elif modeSelect == "2" :
            area.circleArea()
        elif modeSelect == "3" :
            cube.squareCube()
        elif modeSelect == "4" :
            cube.circleCube()
        elif modeSelect == "0" :
            exit
        else :
            print("กรุณาป้อนตัวเลข 0-4")
            selection()
    selection()

except :
    print("กรุณาป้อนตัวเลข 0 - 4")