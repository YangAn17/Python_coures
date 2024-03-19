## 使用 % 运算符
# %s 字符串 %d 整数 %f 浮点数 %x 十六进制整数
print("Hello, %s" % "world")
print("Hi, %s, you have $%d." % ("Michael", 1000000))
print("%2d-%02d" % (3, 1))  # 格式化整数和浮点数还可以指定是否补0和整数与小数的位数
print("%.2f" % 3.1415926)

## 使用 format() 方法
# 用{}和:代替%，后面用format()方法传入参数
print("Hello, {0}, 成绩提升了 {1:.1f}%".format("小明", 17.125))

## 使用 f-string
# 在字符串前面加上f或F，直接把变量放入大括号{}中
r = 2.5
s = 3.14 * r**2
print(f"The area of a circle with radius {r} is {s:.2f}")
