# -*- coding: utf8 -*-
'''
角色类的定义

角色有：
1. 主人公
2. 反派BOSS
3. 小怪
'''

class CCreature(object):
	'''
	生物类定义
	'''	
	def __init__(self):
		self.healthValue = 1
		self.fiveSpiritVal = 
		{
			"metal": 1,
			"wood" : 1,
			"water": 1,
			"fire" : 1,
			"earth": 1
		}
		
	def GetHealthVal(self):
		return self.healthValue
	def SetHealthVal(self, val):
		self.healthValue = val
	
	def GetSomeSpiritVal(self, spiritName):
		return self.fiveSpiritVal[spiritName]
	def SetSomeSpiritVal(self, spiritName, val):
		self.fiveSpiritVal[spiritName] = val
		
		
class CProtagonist(CCreature):
	'''
	主人公类定义
	'''
	def __init__(self):
		super(CProtagonist, self).healthValue = 3

class CBoss(CCreature):
	'''
	反派BOSS类定义
	'''
	def __init__(self):
		#super(CProtagonist, self).healthValue = 5
		CCreature(self).healthValue = 3

class CMonster(CCreature):
	'''
	小怪类定义
	'''
	pass
