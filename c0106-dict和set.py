## dict字典，使用键-值（key-value）存储，具有极快的查找速度
d = {"Michael": 95, "Bob": 75, "Tracy": 85}
print(d["Michael"])  # 95

# 放入字典需增加key，value
d["Adam"] = 67
print(d["Adam"])  # 67

# 赋值
d["Adam"] = 88
print(d["Adam"])  # 88

# pop()方法：删除一个key，value
print(d.pop("Bob"))
print(d)  # {'Michael': 95, 'Tracy': 85}

# in语句：判断key是否存在
print("Thomas" in d)  # False

# get()方法：判断key是否存在，返回None或指定的value
print(d.get("Thomas"))  # None
print(d.get("Thomas", -1))  # -1


## set是一组key的集合，不存储value且key不重复
s = set([1, 2, 3])
print(s)  # {1, 2, 3}

# 重复元素在set中自动被过滤
s = set([1, 1, 2, 2, 3, 3])
print(s)  # {1, 2, 3}

# add(key)方法：添加key
s.add(4)
print(s)  # {1, 2, 3, 4}

# remove(key)方法：删除元素
s.remove(4)
print(s)  # {1, 2, 3}

"""
    set可以看成数学意义上的无序和无重复元素的集合，
    两个set可以做数学意义上的交集、并集等操作
"""
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)  # {2, 3}
print(s1 | s2)  # {1, 2, 3, 4}
