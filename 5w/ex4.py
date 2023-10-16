while True:
    dan = int (input ("dan: "))
    gop = int (input ("gop: "))
    
    if dan <= 0 and gop <= 0:
        continue
    
    print("%d x %d = %d" %(dan, gop, dan*gop))

    
