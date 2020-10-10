name = "小明"

# 调用函数不能在定义函数之前，必须要确保python已经知道函数的存在
# python解释器知道下方定义了一个函数
# ！！！！注意注意！！因为函数相对比较独立，函数定义上方，
#   应该和其他代码（包括注释）保留两个空行


def say_hello():
    """打招呼"""
    
    
    print("hello 1")
    print("hello 2")
    print("hello 3")
    
print(name)

# 只有在程序中，主动调用函数，才会让函数执行
say_hello()

print(name)