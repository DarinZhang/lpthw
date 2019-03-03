# -*- coding: utf-8 -*-

age = raw_input("How old are you?")
height = raw_input("How tall are you?")
weight = raw_input("How much do you weigh?")

print "So, you'r %r old, %r tall and %r heavy." % (
	age, height, weight)

####
#note
# 不会先打印"where are you from?"；而是等待输入后，一起打印出来	
print "where are you from? %s" % raw_input()