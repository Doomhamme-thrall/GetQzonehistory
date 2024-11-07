# import builtins;
# for item in dir(builtins):
#     print(item)
# help(input)

# 定义函数

# def step_calculate(num):
#     result=0;
#     for i in range(num+1):
#         result+=i
#     return result

# print(step_calculate(100))


# def demo(obj):
#     obj += obj
#     print(obj)


# a = "hello"
# print(a)
# demo(a)
# print(a)  # 不可变实参不随形参变化

# b = [1, 2, 3]
# print(b)
# demo(b)
# print(b)  # 可变实参随形参变化


# def full_name(first, last):
#     return first + " " + last


# print(full_name("jhon", "wick"))

# print(full_name(last="wick", first="jhon"))

# def full_name(first,last="wick"):
#     return first + " " + last

# print(full_name("jhon"))
# print(full_name("jhon","snow"))

# 可变长参数
# def func(a,*args):
#     print(a)
#     print(args)
#     print(type(args))

# func(1,2,3,4,5)

# def func(a,**kwargs):
#     print(a)
#     print(kwargs)
#     print(type(kwargs))

# func(1,b=2,c=3,d=4,e=5)

# def func():
#     print("hello")
# 函数名是内存地址
# print(func)

# def sumandaverage(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum, sum / len(args)

# sum = sumandaverage(1, 2, 3, 4, 5)
# print(sum) #返回元组

# def func(a,b):
#     c= a+b
#     return c

# s=func(1,2)
# print(s)
# print(c) #c是局部变量，不能在函数外部访问

# def outer():
#     a = 1

#     def inner():
#         global a
#         a = 200
#         print(a)

#     inner()
#     print(a)

# def outer():
#     a = 1

#     def inner():
#         nonlocal a
#         a = 200
#         print(a)

#     inner()
#     print(a)

# outer()

# def outer():
#     a = 1
#     print("outer:", a)
#     def inner():
#         print(a)

#     print("outer:", a)
#     return inner  闭包

# f=outer()
# f()
# f()


# def func(a):
#     if a == 1:
#         return 1
#     return a * func(a - 1)


# print(func(25))


def func(x):
    return x * x


result = map(func, [1, 2, 3, 4, 5])
print(result)
print(list(result))
