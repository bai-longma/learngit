for row in range(0,10):
    for col in range(0,10-row):
        print(" ",end="")
    for i in range(0,2*row+1):
        print("*",end="")
    print("")