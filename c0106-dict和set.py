## dict字典，使用键-值（key-value）存储，具有极快的查找速度
#
d = {"Michael": 95, "Bob": 75, "Tracy": 85}
print(d["Michael"])  # 95

# 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
d["Adam"] = 67
print(d["Adam"])  # 67

# 赋值给已有的key，会覆盖原有的value
d["Adam"] = 88
print(d["Adam"])  # 88

# 通过in判断key是否存在
print("Thomas" in d)  # False
# 通过get()方法，如果key不存在，可以返回None，或者自己指定的value
print(d.get("Thomas"))  # None
print(d.get("Thomas", -1))  # -1

# 通过pop()方法删除一个key
print(d.pop("Bob"))
print(d)  # {'Michael': 95, 'Tracy': 85}

## set是一组key的集合，不存储value，key不能重复
#
s = set([1, 2, 3])
print(s)  # {1, 2, 3}

# 重复元素在set中自动被过滤
s = set([1, 1, 2, 2, 3, 3])
print(s)  # {1, 2, 3}

# 通过add(key)方法可以添加元素到set中
s.add(4)
print(s)  # {1, 2, 3, 4}

# 通过remove(key)方法可以删除元素
s.remove(4)
print(s)  # {1, 2, 3}

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)  # {2, 3}
print(s1 | s2)  # {1, 2, 3, 4}
