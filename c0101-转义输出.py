## 通用方法
# 转义字符 \ ，用于输出 ' " \ 等特殊字符
print('I\'m "OK"!')
print("I'm learning\nPython.")  # 输出特殊字符，如换行符 \n 制表符 \t
print("\x00")  # 输出不可见字符，如 \x00 \x0a \x0d
print("\u4e2d\u6587")  # 输出 Unicode 字符，如 \u4e2d \u6587

## 简化方法
# 字符串"前面加 r ，表示"内均转义
print(r'I\'m "OK"!')
print(r"I'm learning\nPython.")

## 三引号：输出多行字符串
print(
    """line1
line2
line3"""
)
