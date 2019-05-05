# -*- coding: utf-8 -*-

'''
战斗系统
'''

import figure
scene.LoadTip(u"角色模块导入中", u"角色模块导入成功")

from figure import zhurengong as zhangdafan

MapSpiritName = {
	'metal' = '金',
	'wood' = '木',
	'water' = '水',
	'fire' = '火',
	'earth' = '土'
}

bFirstCombat = True

def CombatTip():
	'''
	战斗系统说明
	'''
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
	print u"战斗双方各有三张五灵符，每张符有各自的五灵属性和五灵值。"
	print u"五灵符根据五灵属性相生相克。"
	print u"若双方五灵符属性一样，则比较五灵值；若五灵值也一样，则平局。"
	print u"战斗双方每次各出一张符。三局两胜。"


def comparSpirit(spiritA, spiritB):
	'''
	根据五行相生相克,判断输赢及平局
	'''
	if spiritA == spiritB:
		return 'tie'
	
	if spiritA == 'metal':
		if spiritB == 'wood' || if spiritB == 'earth':
			return 'win'
		else
			return 'defeat'
	
	if spiritA == 'wood':
		if spiritB == 'earth' || if spiritB == 'water':
			return 'win'
		else 
			return 'defeat'
			
	if spiritA == 'water':
		if spiritB == 'fire' || if spiritB == 'metal':
			return 'win'
		else
			return 'defeat'
	
	if spiritA == 'fire':
		if spiritB = 'metal' || if spiritB == 'wood':
			return 'win'
		else
			return 'defeat'
	
	if spiritA == 'earth':
		if spiritB == 'water' || if spiritB == 'fire':
			return 'win'
		else
			return 'defeat'
	

def Combating(playerB):
	'''
	战斗中，三局两胜
	'''
	CombatTip()
	
	cardsDafan = zhangdafan.GetThreeCard()
	cardsB = playerB.GetThreeCard()
	keysDafan = cardsDafan.keys()
	keysB = cardsB.keys()
	resList = []
	for i in xrange(0, 3):
		spiritDafan = keysDafan[i]
		spiritB = keysB[i]
		res = comparSpirit(spiritDafan, spiritB)
		resList.append(res)
	
	if count('win') >= 2:
		return 'win'
	elif count('defeat') >= 2:
		return 'defeat'
	else
		return 'tie'

def CombatReport():
	'''
	战果统计
	'''
	print u"恭喜，顺利通过本场景。"
	print u"目前，少侠的境界如下："
	print u"<<<生命值: %d", zhangdafan.GetHealthVal()
	print u"<<<", zhangdafan.PrintSomeSpiritVal()
	
	
	
	
	
	
	
	
	
	
