# 定义一个小数 price、weight、money
# 输出 苹果单价 9.00元/斤，购买了 5.00 斤，需要支付 45.00元
price = 9.0
weight = 5.0
money = price * weight
# %f:浮点数，%.2f表示小数点后只显示两位，
# %.0f表示小数点后面没有位数
print("苹果单价 %.0f%% 元/斤,购买了 %.3f 斤，需要支付 %.4f 元" % (price,weight,money))


student_no = 123456
print("我的学号是 %07d" % student_no)
print("我的学号是",student_no)
# 有两种输出方式，%是格式化输出。
# 当最后输出的数据与输入数据不一致的时候，就可以采取格式化输出！


# 同样输出有两种方式，采取格式化输出，
# 最后输出的时候，数据可以更改
print("购买了",weight,"斤")
print("购买了 %.1f 斤" % weight)


# 同样输出变量有两种方式，一种传统方式，一种格式化方式！
name = "小明"
print("我的名字叫",name,",","请多关照！")
print("我的名字叫 %s,请多关照！" % name)