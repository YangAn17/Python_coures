## 用于解决多 if 语句判断的问题，使用 match 语句
# 适用于 Python 3.10 以上版本

# 单变量匹配
score = "B"

match score:
    case "A":
        print("优秀")
    case "B":
        print("良好")
    case "C":
        print("及格")
    case _:
        print("错误输入")

# 复杂匹配：多个值、一定范围、多个条件
age = 15

match age:
    case x if x < 10:
        print(f"< 10 years old : {x}")
    case 10:
        print("10 years old.")
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print("11~18 years old.")
    case 19:
        print("19 years old.")
    case _:
        print("not sure.")

# List 匹配
args = ["gcc", "hello.c", "world.c"]
# args = ['clean']
# args = ['gcc']

match args:
    # 如果仅出现gcc，报错:
    case ["gcc"]:
        print("gcc: missing source file(s).")
    # 出现gcc，且至少指定了一个文件:
    case ["gcc", file1, *files]:
        print("gcc compile: " + file1 + ", " + ", ".join(files))
    # 仅出现clean:
    case ["clean"]:
        print("clean")
    case _:
        print("invalid command.")
