# -*- coding: utf-8 -*-

# 参考《流浪地球》

from sys import exit

def spaceShipPlan():
	print u"您将选择飞船计划"
	print u"请输入您的年龄"
	age = raw_input("> ")
	print u"请输入您的学历"
	education = raw_input("> ")

	#print education.decode('Gbk') == u"硕士"
	# note 1
	# 两个中文字符串比较时，需要统一编码格式
	
	bSeleIntoShip = False
	
	if int(age) <= 10:
		bSeleIntoShip = True
		print u"根据联合政府公约，10岁及以下公民拥有直接登陆宇宙飞船的权利"
		print u"请在10个工作日内，凭公民识别码至附近飞船传送点登船"		
	elif int(age) <= 40 and (education.decode('Gbk') == u"硕士" or education.decode('Gbk') == u"博士" or education.decode('Gbk') == u"博士后"):
		bSeleIntoShip = True
		print u"根据联合政府公约，教育水平较高的中青年公民拥有直接登陆宇宙飞船的权利"
		print u"请在10个工作日内，凭公民识别码至附近飞船传送点登船"
	else:
		print u"由于飞船空间有限，只能容纳部分公民"
		print u"请在15个工作日内，携带公民识别码至附近抽签点进行抽签"
		print u"中签者则获得登陆飞船的权利；未中签者，将留守地球"
	
	if bSeleIntoShip == True:
		print u"祝您好运，再见"
		return
	else:
		print u"是否重新选择方案？请输入'是'或'否'"
		decide = raw_input("> ")
		
		if decide.decode('Gbk') == u'是':
			print u"祝您好运，再见"
			return
		else:
			start()	
			
	
def wanderingEarthPlan():
	print u"您将选择流浪地球计划"
	print u"请选择您的职业"
	print u"a. 学生"
	print u"b. 物理学家"
	print u"c. 程序员"
	print u"d. 建筑师"
	print u"e. 数学家"
	print u"f. 天文学家"
	print u"g. 其他"
	profess = raw_input("> ")
	
	if profess == 'a':
		print u"请携带公民识别码，在15个工作日内进入附近地下城"
		print u"希望你好好学习，日后能在流浪地球计划中做出更大贡献"
	elif profess == 'b' or profess == "e":
		print u"请携带公民识别码，在15个工作日内进入附近联合政府传送点"
		print u"您将进入联合政府智囊团工作，为流浪计划出谋划策"
	elif profess == 'c' or profess == 'f':
		print u"请携带公民识别码，在15个工作日内进入附近联合政府传送点"
		print u"您将被派遣至领航者号空间站，为地球流浪之旅领航"
	else:
		print u"请携带公民识别码，在15个工作日内进入附近行星发送机点"
		print u"您将参与行星发动机的建筑工作"
	
	print u"谢谢您的配合"
	print u"地球是我们的家园,感谢你我做出的努力"
	print u"祝您好运，谢谢"	

	
def start():
	print u"请您在以下方案，做出选择"
	print u"a. 制造尽可能大的宇宙飞船，带着人们星际穿越至适合人类生存的星系"
	print u"b. 在地球一面安装数千座发动机，推动整个地球飞行至适合人类生存的星系"
	print u"c. 给出你自己的方案"
	
	choice = raw_input("> ")
	
	if choice == 'a':
		spaceShipPlan()
	elif choice == 'b':
		wanderingEarthPlan()
	elif choice == 'c':
		print u"请将您的方案以Email的形式发送至联合政府未来可持续发展办公室邮箱fof@lhzf.cn"
		print u"我们会认真分析方案的可行性，并在15个工作日给出回复"
		print u"谢谢您的参与。再见"
		return
	else:
		start()
		
print u"太阳急速老化。科学家预计几百年后，太阳将膨胀并吞噬掉地球"
start()


# notes
# 概率出现此脚本在别人的cmd或powershell上运行时，部分中文显示乱码，还会异常退出。
# 目前解决方法是：
#     在cmd或powershell上输入：
#     chcp 65001  
#     chcp 936
# 输入上述两个命令后，再运行脚本就正常了
# 具体什么原因还没搞清楚，或者这个是Python或cmd/powershell的BUG？
# chcp 65001 # 换成utf-8格式
# chcp 936   # 换成默认的gbk
# chcp 437   # 换成美国英语
# 具体参考https://www.cnblogs.com/sunshuhai/p/6242275.html