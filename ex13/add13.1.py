# -*- coding: utf-8 -*-

from sys import argv

# 个人信息调查问卷

script, name, age, height, weight, hometown = argv

print "\nPlease verify the personal information you entered:\n"

checkName = "\t Is your name %r? Y(es) or N(o):" % name
raw_input(checkName)
checkAge = "\t Is your age %r? Y(es) or N(o):" % age
raw_input(checkAge)
checkHeight = "\t Is your heigth %r? Y(es) or N(o):" % height
raw_input(checkHeight)
checkWeight = "\t Is your weight %r? Y(es) or N(o):" % weight
raw_input(checkWeight)
checkHt = "\t Is your hometown %r? Y(es) or N(o):" % hometown
raw_input(checkHt)

print '''
Thanks for your response!
Bye!
'''