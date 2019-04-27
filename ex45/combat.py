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

def Combating(playerA, playerB):
	CombatTip()
	
	
	
		

