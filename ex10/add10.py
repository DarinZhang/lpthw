# -*- coding: utf-8 -*-

import time

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."


# ''' is equal to """
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
'''

print "test1: %s" % tabby_cat
print "test2: %r \n" % tabby_cat
print "test3: %s" % persian_cat
print "test4: %r \n" % persian_cat
print "test5: %s" % backslash_cat
print "test6: %r \n" % backslash_cat
print "test7: %s" % fat_cat
# Every line will be added with '\n', and "'''" also becomes '\n'
print "test8: %r \n" % fat_cat

#notes
#1. %r 是调试用的，%s 是显示输出用的。
#2. 遇到问题或不懂的，用小本记下。定期检查小本，把不懂的都要弄明白，及定期复习。
