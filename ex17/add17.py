# -*- coding: utf-8 -*-

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

indata = (open(from_file)).read()
(open(to_file, 'w')).write(indata)

print "Alright, all done."

#notes
# to do: 文件open()后，但没有close()，不太安全，但是脚本运行结束后，文件也会自动close()的
# ？ Zed说能写成一行，是不是用的什么现成的拷贝接口？