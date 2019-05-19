# -*- coding: utf-8 -*-

'''
战斗系统
'''

# 模块相互import,报错
# scene中import combat; combat中import scene
# import scene
# scene.LoadTip(u"战斗系统导入中", u"战斗系统导入成功")

import time

def DelaySleep():
	'''
	线程睡眠
	'''
	time.sleep(2)

def LoadTip(stat, res):
	"""
	场景加载提示语
	"""
	for i in xrange(1, 4):
		print stat, "..."*i
		time.sleep(1)
	print res, '\n'

LoadTip(u"战斗系统导入中", u"战斗系统导入成功")	


import figure
from figure import zhurengong as zhangdafan
LoadTip(u"角色模块导入中", u"角色模块导入成功")	

MapSpiritName = {
	'metal': u'金',
	'wood' : u'木',
	'water' : u'水',
	'fire' : u'火',
	'earth' : u'土'
}

bFirstCombat = True

def CombatTip():
	'''
	战斗系统说明
	'''
	global bFirstCombat
	
	if bFirstCombat:
		bFirstCombat = False
		print u"这是您第一次进入战斗系统。请仔细阅读下面的战斗规则。"
		PrintRule()
	else:
		print u"是否需要回顾下战斗规则？ 是[Y] 否[N]"
		res = raw_input("> ")
		if res == 'Y':
			PrintRule()

def PrintRule():
	'''
	战斗规则说明
	'''
	DelaySleep()
	print u"战斗双方各有三张五灵符，每张符有各自的五灵属性和五灵值。"
	DelaySleep()
	print u"五灵符根据五灵属性相生相克。"
	DelaySleep()
	print u"若双方五灵符属性一样，则比较五灵值；若五灵值也一样，则平局。"
	DelaySleep()
	print u"战斗双方每次各出一张符。三局两胜。"
	DelaySleep()
	print u"若战斗获胜，则对方的五灵值归你所有；否则，你的生命值减一。"
	DelaySleep()


def comparSpirit(spiritA, spiritB):
	'''
	根据五行相生相克,判断输赢及平局
	'''
	if spiritA == spiritB:
		return 'tie'
	
	if spiritA == 'metal':
		if spiritB == 'wood' or spiritB == 'earth':
			return 'win'
		else:
			return 'defeat'
	
	if spiritA == 'wood':
		if spiritB == 'earth' or spiritB == 'water':
			return 'win'
		else: 
			return 'defeat'
			
	if spiritA == 'water':
		if spiritB == 'fire' or spiritB == 'metal':
			return 'win'
		else:
			return 'defeat'
	
	if spiritA == 'fire':
		if spiritB == 'metal' or spiritB == 'wood':
			return 'win'
		else:
			return 'defeat'
	
	if spiritA == 'earth':
		if spiritB == 'water' or spiritB == 'fire':
			return 'win'
		else:
			return 'defeat'
	

def Combating(playerB):
	'''
	战斗中，三局两胜
	'''
	CombatTip()
	
	cardsDafan = zhangdafan.GetThreeCard()
	cardsB = playerB.GetThreeCard()
	print u"你的五灵符: "
	cardsDafan.PrintItems()
	print u"对方的五灵符: "
	cardsB.PrintItems()
	
	keysDafan = cardsDafan.GetKeys()
	keysB = cardsB.GetKeys()
	valuesDafan = cardsDafan.GetValues()
	valuesB = cardsB.GetValues()	
	resList = []
	for i in xrange(0, len(keysDafan)):
		spiritDafan = keysDafan[i]
		spiritB = keysB[i]
		res = comparSpirit(spiritDafan, spiritB)
		if res == 'tie':
			# 五灵属性相同时，比较五灵值
			spValDafan = valuesDafan[i]
			spValB = valuesB[i]
			if spValDafan == spValB:
				res = 'tie'
			elif spValDafan > spValB:
				res = 'win'
			else:
				res = 'defeat'
			
		resList.append(res)
	
	if resList.count('win') >= 2:
		print u"恭喜，战斗获胜。"
		return 'win'
	elif resList.count('defeat') >= 2:
		print u"抱歉，战斗败北。"
		return 'defeat'
	else:
		print u"战斗平局。"
		return 'tie'

def CombatReport():
	'''
	战果统计
	'''
	print u"目前，少侠的境界如下："
	print u"<<< 生命值: %d" % zhangdafan.GetHealthVal()
	zhangdafan.PrintSomeSpiritVal()
	
	
	
	
	
	
	
	
	
	
