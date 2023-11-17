def BBL_Sort():
    Lst = [1,4,77,12,5,60]
    for i in range (0, len(Lst)):
        for J in range (0, len(Lst)-1):
            if Lst [J] > Lst [J+1]:
                TEMP = Lst [J]
                Lst[J] = Lst [J+1]
                Lst [J+1] = TEMP
    print (Lst)

BBL_Sort()