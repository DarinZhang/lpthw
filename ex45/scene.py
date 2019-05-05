# -*- coding: utf-8 -*-

'''
各种场景类的定义

场景包括：
0. 开篇  --->   Start
1. 十里坡（练级）   --->   GreenHandsHamlet
2. 风波店（卷入江湖追杀）   --->   DisturbanceShop
3. 东海死火山（奇遇练得神功） --->   ExtinctVolcanoInEastChinaSea
4. 修罗院（探寻真相，英雄救美，临危受命）  --->   ShuraGarden
5. 少林寺（英雄大会，拯救江湖）  --->   ShaolinTemple
6. 通关成功（携美人归隐山林） --->   Pass
7. 通关失败（死亡）  --->  Defeat
7. 从头再来  --->  Again
8. 退出游戏  --->  Exit
'''

import time
import combat

def LoadTip(stat, res):
	"""
	场景加载提示语
	"""
	for i in xrange(1, 4):
		print stat, "..."*i
		time.sleep(1)
	print res, '\n'

def DelaySleep():
	'''
	线程睡眠
	'''
	time.sleep(2)

class CScene(object):
	'''
	场景基类
	'''	
	def __init__(self):
		LoadTip(u"场景加载中，少侠请稍候", u"场景加载成功")
		# 记录下一个场景
		self.nextScene = 'Pass'
		
	def Enter(self):
		# 进入场景
		pass
	
	def GetNextScene(self):
		# 返回下一个场景
		return self.nextScene
	
class CscStart(CScene):
	'''
	开篇
	'''
	def __init__(self):
		CScene(self).__init__()
		
	def Enter(self):
		print u"=====南宋末年，余杭镇====="
		print u"刚经历冠礼的张大凡闲着无聊，和隔壁的小虎去秧田里捕鱼。"
		DelaySleep()
		print u"半天下来，鱼一条没捕到，却把邻居们田里的秧苗都踩坏了。"
		DelaySleep()
		print u"因此，刚成年的张大凡就被爹娘狠狠地双打了一顿。"
		DelaySleep()
		print u"气愤之余，张大凡离家出走，刚出村口，就撞上一个黑衣人躺在地上，脸上一道刀疤，身上满是鲜血。"
		DelaySleep()
		print u"走进一看，此人已断气。黑色的衣衫下隐约看到一本书和一颗亮晶晶的珠子。"
		DelaySleep()		
		print u"张大凡捡起书,看了看书名。"
		print u"!!!你希望书名是："
		print u"1. 炼金术"
		print u"2. 木剑术"
		print u"3. 驭水术"
		print u"4. 火球术"
		print u"5. 落石术"
		bookName = raw_input("> ")
		
		if bookName == '1':
			print u"习得炼金术"
			zhangdafan.AddSomeSpiritVal('metal', 1)
		elif bookName == '2':
			print u"习得木剑术"
			zhangdafan.AddSomeSpiritVal('wood', 1)
		elif '3' == bookName:
			print u"习得驭水术"
			zhangdafan.AddSomeSpiritVal('water', 1)
		elif bookName == '4':
			print u"习得火球术"
			zhangdafan.AddSomeSpiritVal('fire', 1)
		else:
			print u"习得落石术"
			zhangdafan.AddSomeSpiritVal('earth', 1)
			
		print u"张大凡捡起珠子。"
		print u"你希望珠子颜色是："
		print u"1. 金色"
		print u"2. 绿色"
		print u"3. 蓝色"
		print u"4. 红色"
		print u"5. 黄色"
		beadColor = raw_input("> ")
		
		if bookName == '1':
			zhangdafan.GainSpiritBead('metal')
		elif bookName == '2':
			zhangdafan.GainSpiritBead('wood')
		elif '3' == bookName:
			zhangdafan.GainSpiritBead('water')
		elif bookName == '4':
			zhangdafan.GainSpiritBead('fire')
		else:
			zhangdafan.GainSpiritBead('earth')		
		
		print u"这个人为什么会倒在村口呢？身上的剑伤哪来的？一系列的疑问萦绕在张大凡心头。"
		print u"出于好心，张大凡给他入土为安，给他立了无名碑。"
		# 下一场景:十里坡（练级）
		self.nextScene = 'GreenHandsHamlet'

class CScGreenHandsHamlet(CScene):
	'''
	 十里坡（新手村）
	'''
	def __init__(self):
		super(CSceneGreenHandsHamlet, self).__init__()
		print u"\n\n****半个月后****"
		print u"听说村外十里坡最近经常出现妖怪伤人事件。近几个月，爹娘都会去那附近采药。"
		DelaySleep()
		print u"实在不放心，决定前去一探究竟。"
		DelaySleep()
		
	def Enter(self):
		print u"\n====十里坡====\n"
		print u"天气晴朗，万里无云。十里坡还是如幼时记忆中的一样，绿草如茵，鸟语花香。"
		DelaySleep()
		print u"并不像村民中口所说的不太平。不如四处走走，就当春游了。"
		DelaySleep()
		print u"突然不远处传来一阵孩童的哭喊声。上前一看，一个六、七岁的男童被几个长得奇形怪状的"
		DelaySleep()
		print u"妖兽包围着。妖兽长着獠牙，爪牙锋利，随时欲扑上去伤害男童。"
		DelaySleep()
		print u"!!!赶紧诛杀这些妖兽。"
		
		# 进入战斗系统
		# 杀三个小鬼
		for i in xrange(0, 3):
			monster = figure.CMonster()
			res = combat.Combating(monster)
			
			if res == 'win':
				# 对方的五灵值归自己所有
				zhangdafan.AddSomeSpiritVal(monster)
			elif res == 'defeat':
				# 生命值减一
				zhangdafan.ReduceHealthVal(1)
				if False == zhangdafan.IsAlive():
					self.nextScene = 'Defeat'
					return
		
		combat.CombatReport()
		self.nextScene = 'DisturbanceShop'
		
		print u"妖兽几乎都被诛杀。其中一只妖兽躺在地上，奄奄一息，快断气前说道："
		print u"风波店中的天行刀主是你什么人？你为什么会他的武功道法？哼，别得意，我们鬼面门不会放过"
		print u"天玄宗的，你们都等死吧！！！"
		print u"说完，那只妖兽便断气了。\n\n"
		print u"天行刀主？鬼面门？天玄宗？张大凡一时间不知道这些是什么。带着疑虑，张大凡把孩子送回了家。"
		
		
class CScDisturbanceShop(CScene):
	'''
	风波店（卷入江湖追杀）
	'''
	def __init__(self):
		DelaySleep()
		print u"\n\n\n夜深人静，窗外星光点点，蛙声一片。"
		print u"张大凡躺在窗口，怎么都睡不着。白天的事情始终没搞清楚。"
		print u"听村里说书先生说过，天玄宗是中原大陆上第一修仙门派，天行刀主是天玄宗的三元老之一。"
		print u"而鬼面门则是第一魔教，门中包括修炼魔功的魔人，及各类妖魔。"
		print u"听说，天行刀主常穿黑衣，脸上有一处刀疤。难道半个月前，在村口遇到的黑衣人就是天行刀主？"
		print u"到底什么人能杀死天行刀主？从妖兽的话里可以推断出，鬼面门意图对付天玄宗。显然，鬼面门已经开始行动。"
		print u"鬼面门究竟有什么阴谋？要怎么对付天玄宗？"
		print u"好多问题困扰着张大凡。看来只能去一趟妖兽提到的风波店，看看能不能发现什么蛛丝马迹。"
		
	
	
	



