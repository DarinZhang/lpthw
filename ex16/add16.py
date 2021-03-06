# -*- coding: utf-8 -*-

from sys import argv
import os

script, filename = argv

print "We're going to erase %r" % filename
print "If you don't want that, hit CTRL-C(^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Open the file ..."
target = open(filename, 'w+')

print "Truncating the file. Goodbye!"
# notes
# 当以模式'w'或'w+'打开文件时
# 若文件已经存在，则清空其中内容，然后从头开始写入;
# 若文件不存在，则自动新建文件
# 所以下面的truncate()可以省略
# target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

newCont = "%s \n%s \n%s \n" % (line1, line2, line3)
target.write(newCont)

print "Now Let's print the file:"
# notes
# 若此时立即read()，是读不出刚才写入的内容的。
# 因为write()只是将内容写入缓存中，并没有写入磁盘中的文件里。
print "First print"
print target.read()  # 显示为空
# 将write()的写入缓存的内容，写入磁盘的方法有：
# 1. close()文件
# 2. flush()，强制将缓存中的内容写入磁盘，但注意要配合os.fsync()使用。
#    具体请参考官方https://docs.python.org/2/library/stdtypes.html?highlight=file%20flush#file.flush
target.flush()
os.fsync(target)
target.seek(0)
print "Second print"
print target.read() # 显示刚才写入的内容了

print "And finally, we close it."
target.close()



