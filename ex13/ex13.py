# -*- coding: utf-8 -*-

from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third


#####
# notes
# 1.上述方式传入的参数都被解包为字符串类型 
# python ex13.py 123 apple 'banana'
print type(script)    # <type'str'>
print type(first)     # <type'str'>
print type(second)    # <type'str'>
print type(third)     # <type'str'>