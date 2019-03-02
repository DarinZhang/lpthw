# -*- coding:utf-8 -*-

# 变量x赋值为字符串"There are 10 types of people."
x = "There are %d types of people." % 10
# 变量binary赋值为字符串"binary"
binary = "binary"
# 变量do_not赋值为字符串"don't" 
do_not = "don't"
# 变量y赋值为字符串"Those who know binary and those who don't."
y = "Those who know %s and those who %s." % (binary, do_not)
             #StrInStr POS1     #StrInStr POS2     
print x
print y

# 将变量x格式化输出为"I said: %r." 
print "I said: %r." % x
		 #StrInStr POS3 

# 将变量y格式化输出为"I also said: '%s'."
print "I also said: '%s'." % y
			   #StrInStr POS4
				
# 变量hilarious赋值为布尔型常量False
hilarious = True

# 变量joke_evaluation赋值为字符串"Isn't that joke so funny?! %r"(包含一个不确定的格式化输出)
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

# 变量w赋值为字符串"This is the lef side of ..."
w = "This is the left side of ..."
# 变量e赋值为字符串"a string with a right side."
e = "a string with a right side."

# 将字符串变量w和e连接后，打印输出
print w + e


#################
#notes
#1. %r格式化输出，变量原始的数据值
#2. 运算符 '+' 可用于字符串拼接

