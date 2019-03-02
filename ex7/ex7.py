# -*- coding:utf-8 -*-


print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10 # what'd that do?  # print 10 character '.' in a line


end1 = "C"
end2 = "h"
end3 = "e"
end4 = 'e'
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
# if have comma, the second print will be in the same line with the first print.
# othewise, the second print will be in a new line.
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12


#notes
#1. 字符串 * number, 代表重复number份字符串。
#2. 字符串过长时，可用逗号','分成多行书写，但中间会有个空格。
#   所以最好是在本来就有空格的地方用','分行写。
