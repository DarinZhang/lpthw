# -*- coding: utf-8 -*-

# 从模块sys导入argv
from sys import argv
# argv解码赋值给变量script和filename
script, filename = argv
# 打开名为变量filename的文件，
txt = open(filename)

print "Here's your file %r:" % filename
# 读取文件对象对应的文件内容，并打印出来
print txt.read()

print "Type the filename again:"
prompt = "> "
file_again = raw_input(prompt)

txt_again = open(file_again)

print txt_again.read()