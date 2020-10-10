for row in range(0,10):
    for col in range(0,row):
        print(" ",end="")
    for i in range(0,2 * (10-row)-1):
        print("*",end="")
    print("")