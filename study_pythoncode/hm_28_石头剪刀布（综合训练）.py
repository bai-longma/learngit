# 导入随机工具包
# 注意：再导入工具包的时候，应该将导入的语句，放在文件的顶部
# 因为，这样可以方便下方的代码，在任何需要的时候，使用工具包中的工具

import random

# 从控制台输入要出的拳 —— 石头（1）/剪刀（2）/布（3）
player = int(input("请输入您要出的拳 石头（1）/剪刀（2）/布（3）："))


# 电脑 随机 出拳 —— 先假定电脑只会出石头，完成整体代码功能
# computer = 1

# 改进电脑出拳的随机性，在代码最开始导入模块
# 并且使用随机random这个工具包中的随机整数randint这个函数！
computer = random.randint(1,3)

print("玩家出的拳是 %d - 电脑出的拳是 %d " % (player,computer))


# 比较胜负 
# 1 石头 胜 剪刀
# 2 剪刀 胜 布
# 3 布 胜 石头
# if () or () or ():
# !!!!在if () or () or (): 加上一对()，就变成if (() or () or ()):
# 并且有利于阅读代码，在or之间分行，同时为了不与print函数混淆，前面用Tab键空8个空格！！！

# 注意！！！在python 中怎么将一个很长很长的逻辑表达式进行换行调整格式！！
# 一句话讲，在大的条件前，和大的条件后，增加一对小括号，增加完后后，在一个小的逻辑运算符前面增加一个换行！！
# ！！并且增加8个空格的缩进，以此保证代码的阅读！！
# 并且 在条件与输出过程中，空一行，便于阅读！

if ((player == 1 and computer == 2) 
        or (player == 2 and computer == 3) 
        or (player == 3 and computer == 1)):
    
    print("欧耶，电脑弱爆了！") 
    
# 如果平局的情况
elif player == computer:
    print("真是心有灵犀啊，再来一盘")

# 其他情况电脑获胜
else:
    print("不服气，我们决战到天明！")