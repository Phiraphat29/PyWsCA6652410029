import random 

print("-----------------GUESS THE NUMBER!!!-----------------")
luckyNumber = random.randint(1,100)

def checkNum() :
    try :
        guessNum = int(input("Guess Number between 1 - 100: "))
        if guessNum == luckyNumber : 
            print("ยินดีด้วย คุณทายถูก")
        elif guessNum < luckyNumber :  
            print("คุณทายผิด ตัวเลขที่ป้อนน้อยไป")
            checkNum()
        elif guessNum > luckyNumber :
            print("คุณทายผิด ตัวเลขที่ป้อนมากไป")
            checkNum()
    except ValueError :
        print("ต้องเป็นตัวเลขเท่านั้น")
        checkNum()
    
checkNum()

