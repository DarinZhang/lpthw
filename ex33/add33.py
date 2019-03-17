# -*- coding: utf-8 -*-

def GetNumberList(beginNum, endNum, step):
	if (endNum - beginNum) * step <= 0:
		return u"警告：您输入的参数无效，无法产生出列表！"
	
	elementsList = []
	element = beginNum
	
	if step > 0:
		while element < endNum:
			elementsList.append(element)
			element += step
	else:
		while element > endNum:
			elementsList.append(element)
			element += step
	
	return elementsList


beginNum = 1
endNum = 1
step = 1
print GetNumberList(beginNum, endNum, step)

beginNum = 1
endNum = 10
step = 0
print GetNumberList(beginNum, endNum, step)

beginNum = 1
endNum = 10
step = 2
print GetNumberList(beginNum, endNum, step)

beginNum = 10
endNum = 3
step = -1
print GetNumberList(beginNum, endNum, step)