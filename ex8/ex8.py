# -*- coding: utf-8 -*-

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it did't sing.",
	"So I said goodnight."
)

##########
#notes
#1. %r 打印中文为unicode编码，建议换用 %s 打印中文
print "test from %r." % "中国"
print "test from %r." % u"中国"
print "test from %s." % u"中国"