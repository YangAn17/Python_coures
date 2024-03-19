## list是一种有序的集合，可以随时添加和删除其中的元素
classmates = ["Michael", "Bob", "Tracy"]
print(classmates)

# len() 函数可以获得list元素的个数
print(len(classmates))

# append() 方法可以追加元素到list末尾
classmates.append("Adam")
print(classmates)

# insert() 方法可以把元素插入到指定的位置
classmates.insert(1, "Jack")
print(classmates)

# pop() 方法可以删除list末尾的元素
classmates.pop()
print(classmates)

# pop(i) 方法可以删除list指定位置的元素
classmates.pop(1)
print(classmates)

# list中的元素也可以直接赋值
classmates[1] = "Sarah"
print(classmates)


## tuple是一种有序的集合，一旦初始化就不能修改
# 为了避免歧义，tuple定义时，元素后面加上逗号
t = 1
print(t)  # 这是一个数
t = (1,)
print(t)  # 这是一个tuple

"""
    tuple所谓的不变是说指向的元素不变，
    即指向'a'，就不能改成指向'b'，但指向的'a'本身是可变的
"""
t = ("a", "b", ["A", "B"])
t[2][0] = "X"
t[2][1] = "Y"
print(t)
