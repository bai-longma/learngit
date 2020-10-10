# 封装九九乘法表到 multiple_table这个函数，
# 然后调用这个函数就可以使用九九乘法表
def multiple_table():
    
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