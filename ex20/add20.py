# -*- coding: utf-8 -*-

# 从模块sys导入对象argv
from sys import argv

# 将对象argv解包为参数script, input_file
script, input_file = argv

# 定义函数print_all(),读取并打印参数对象f的全部内容
def print_all(f):
	print f.read()

# 定义函数rewind()，将对象f的游标归置为0，即开始处
def rewind(f):
	f.seek(0)
	
# 定义函数print_a_line()，打印line_count,以及对象f的一行内容
def print_a_line(line_count, f):
	print line_count, f.readline(),

# 打印文件input_file
current_file = open(input_file)

print "First let's print the whole file:\n"

# 打印对象current_file的全部内容
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# 将对象current_file的游标归0
rewind(current_file)

print "Let's print three lines:"

# 对象current_line赋值为1
current_line = 1
print "current_line: %r" % current_line
print_a_line(current_line, current_file)

# 对象current_line加一后，再赋值给对象current_line
current_line += 1
print "current_line: %r" % current_line
print_a_line(current_line, current_file)

# 对象current_line加一后，再赋值给对象current_line
current_line += 1
print "current_line: %r" % current_line
print_a_line(current_line, current_file)

