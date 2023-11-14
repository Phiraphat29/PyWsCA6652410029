try :
    sentence = input("Enter Your Sentence: ")

    getDup = sentence.split()
    print(f"มีคำรวมทั้งหมด {len(getDup)} คำ ")
    sameWord = list()

    for i in getDup:
        numDup = getDup.count(i)
        if numDup > 1 :
            sameWord.append(i)

    sameWord = set(sameWord)
    print(f"มีคำซ้ำกันรวม {len(sameWord)} คำคือ {' '.join(str(i) for i in sameWord)} ")

    filterWords = list()
    for i in getDup :
        numPerDup = getDup.count(i)
        if numPerDup > 1 and not filterWords.count(i) > 0 :
            filterWords.append(i)
            print(f"คำว่า {i} ซ้ำกัน {numPerDup} ครั้ง ")

except :
    print("Exceptions caught")