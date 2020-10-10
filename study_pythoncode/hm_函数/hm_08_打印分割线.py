# 需求1，定义一个 print_line 函数能够打印 * 组成的一条分割线
def print_line():
    
    
    print("*" * 50)
    
print_line()



#  需求2，定义一个函数能够打印 由任意字符组成 的分割线
def print_line(char):
    
    print(char * 50)
    
print_line("ha")


# 需求3，定义一个函数能够打印 任意重复次数的 分割线
def print_line(char,times):
    
    
    print(char * times)
    
print_line("lala",10)