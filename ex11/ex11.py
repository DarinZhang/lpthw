# -*- coding: utf-8 -*-

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you'r %r old, %r tall and %r heavy." % (
	age, height, weight)
	
#########
#1. raw_input()的使用方式
raw_input("Who are you? ")
raw_input("Where are you from? ")
raw_input("Where will you go? ")

#2. input vs raw_input
# input()认为输入的都是数字，输出按照相关的类型输出。（输入数字，输出数字；输入字符串，输出字符串）
# raw_input()认为输入的都是字符串，且输出的也都是字符串。
a = raw_input("Int: ")   # enter a number
print type(a)
b = input("Int: ")       # enter a number
print type(b)

print u"This is chinese(这是中文)"

