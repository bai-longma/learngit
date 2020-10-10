# 1、打印 9 行小星星



row = 1

while row <= 9:
    
    col = 1
    
    while col <= row:
        
        #print("*",end="")
        #print("9 * 9 = 81",end="  ")
        #print("9 * %d = 81" % row,end="  ")
        print("%d * %d = %d" % (col,row,col*row),end="\t")
        
        col += 1
        
    print("")
    
    
    row += 1