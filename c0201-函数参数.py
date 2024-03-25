# 位置参数： def power(x, n) x和n是位置参数
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# 默认参数： def power(x, n=2) n是默认参数
# * 注意：默认参数需在必选参数后面
# ! 警告：默认参数必须指向不变对象
def power_default(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power_default(5))  # 可以正常运行
print(power_default(5, 3))  # 可以正常运行
# power(5)  # 缺少参数会报错


# 可变参数： def calc(*numbers) *numbers是可变参数
# * 注意：可变参数能传入0个/任意个参数，这些可变参数在函数调用时自动组装为一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2, 3))
print(calc())

nums = [1, 2, 3]
print(calc(nums[0], nums[1], nums[2]))  # 传入list或tuple基本方法是单独传入元素
print(calc(*nums))  # " *nums "表示把nums这个list的所有元素作为可变参数传进去


# 关键字参数： def person(name, age, **kw) **kw是关键字参数
# * 注意：关键字参数能传入0个/任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print("name:", name, "age:", age, "other:", kw)


person("Michael", 30)
person("Bob", 35, city="Beijing")

extra = {"city": "Beijing", "job": "Engineer"}
person("Jack", 24, city=extra["city"], job=extra["job"])  # 传入dict的方法
person(
    "Jack", 24, **extra
)  # " **extra "表示把extra这个dict的所有key-value用关键字参数传进去


# 命名关键字参数： def person(name, age, *, city, job) *后面的参数被视为命名关键字参数
def person_named(name, age, *, city, job):
    print(name, age, city, job)


# 参数检查： isinstance()用于判断变量类型是否是指定的类型
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand type")
    if x >= 0:
        return x
    else:
        return -x


# my_abs("A")  # TypeError: bad operand type
