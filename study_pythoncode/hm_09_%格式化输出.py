# 定义一个小数 price、weight、money
# 输出 苹果单价 9.00元/斤，购买了 5.00 斤，需要支付 45.00元
price = 9.0
weight = 5.0
money = price * weight
print("苹果单价 %.2f%% 元/斤,购买了 %.3f 斤，需要支付 %.4f 元" % (price,weight,money))


student_no = 100123456
print("我的学号是 %d" % student_no)
print("我的学号是",student_no)
# 有两种输出方式，%是格式化输出。
# 当最后输出的数据与输入数据不一致的时候，就可以采取格式化输出！





print("购买了",weight,"斤")
print("购买了 %.1f 斤" % weight)