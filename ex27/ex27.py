# -*- coding: utf-8 -*- 

# 有C/C++或其他编程语言的基础，布尔值不难理解
# 下面为简单地测试

def is_greater_than(a, b):
	return a > b

a = int(raw_input("Please enter an integer: "))
b = int(raw_input("Another again: "))
print "%d > %d ? The answer is %r" % (a, b, is_greater_than(a, b))
# 打印布尔对象类型
print type(is_greater_than(a, b))