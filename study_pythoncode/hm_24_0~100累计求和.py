# -*- coding: utf-8 -*-
# 计算 0~100 之间所有数字的累计求和结果
result = 0

# 1.定义一个整数的变量记录循环的次数
i = 0


# 2.开始循环
while i <= 3:
    print(i)
    
    
    # 每一次循环，都让 result 这个变量和 i 这个计数器相加
    result += i
    
    # 处理计数器
    i += 1
    #result += i
print("0~100之间的数字求和结果 = %d" % result)

