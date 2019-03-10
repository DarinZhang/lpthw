# -*- coding: utf-8 -*-

# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1
	
# this one takes no arguments
def print_none():
	print "I got nothin'."

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()


#notes
# 1. 故意犯错
# print_two("Zed")
# print_one(123, "Darin")
# print_none("")

# 2. 
# 调试时，发现一个函数内，如果一会儿自己敲4格空格缩进，一会儿使用TAB缩进，
# 运行时，会报错 "IndentationError: unexpected indent"
# 需要统一缩进格式，要么统一用TAB，要么统一用4格空格