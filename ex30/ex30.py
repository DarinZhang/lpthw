# -*- coding: utf-8 -*-

people = 30
cars = 40
trucks = 15

# 汽车是否比人多
if cars > people:
	print "We should take the cars."
# 汽车是否比人少
elif cars < people:
	print "Web should not take the cars."
# 汽车是否等于人
else:
	print "We can't decide."

# 卡车是否比汽车多
if trucks > cars:
	print "That's too many trucks."
# 卡车是否比汽车少
elif trucks < cars:
	print "Maybe we could take the trucks."
# 卡车是否等于汽车
else:
	print "We still can't decide."
	
# 人是否比卡车多
if people > trucks:
	print "Alright, let's just take the trucks."
# 人是否小于等于卡车
else:
	print "Fine, let's stay home then."
	