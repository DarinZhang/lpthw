# -*- coding: utf-8 -*-
print "Hello World!"
print "Hello Again"
print "I like typing this."
print "This is fun."
print 'Yay! Printing.'
print "I'd much rather you 'not'."
print 'I "said" do not touch this.'
print "添加一行 你好，世界"  #中文乱码。因为用来显示的控制台使用gbk编码。参考：https://www.cnblogs.com/baihuitestsoftware/articles/5230351.html
print u"添加一行 你好，世界"
print "添加一行 你好，世界".decode("utf-8")