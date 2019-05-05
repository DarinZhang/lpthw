# -*- coding: utf8 -*-
'''
角色类的定义

角色有：
1. 主人公
2. 反派BOSS
3. 小怪
'''

from random import randint

class CCreature(object):
	'''
	生物类定义
	'''	
	def __init__(self):
		self.healthValue = 1
		self.fiveSpiritVal = {
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
	def AddHealthVal(self, val):
		self.healthValue += val
	def ReduceHealthVal(self, val):
		self.healthValue -= val
	def IsAlive(self):
		if self.healthValue <= 0:
			return False
		else:
			return True
	
	def GetSomeSpiritVal(self, spiritName):
		return self.fiveSpiritVal[spiritName]
	def SetSomeSpiritVal(self, spiritName, val):
		self.fiveSpiritVal[spiritName] = val
	def AddSomeSpiritVal(self, spiritName, val):
		self.fiveSpiritVal[spiritName] += val
	def ReduceSomeSpiritVal(self, spiritName val):
		self.fiveSpiritVal[spiritName] -= val
	def PrintSomeSpiritVal(self):
		print "金:%d 木:%d 水:%d 火:%d 土:%d" % self.fiveSpiritVal
		
	def GetThreeCard(self):
		cards = {}
		for i in xrange(0, 3):
			index = randint(1,5)
			
			if index == 1:
				key = 'metal'
			elif index == 2:
				key = 'wood'
			elif index == 3:
				key = 'water'
			elif index == 4:
				key = 'fire'
			else 
				key = 'earth'
			cards[key] = GetSomeSpiritVal(self, key)
			
		return cards
	
	def AddSpiritForWin(self, opponent):
		AddSomeSpiritVal(self, 'metal', opponent.GetSomeSpiritVal('metal'))
		self.AddSomeSpiritVal(self, 'wood', opponent.GetSomeSpiritVal('wood'))
		self.AddSomeSpiritVal(self, 'water', opponent.GetSomeSpiritVal('water'))
		self.AddSomeSpiritVal(self, 'fire', opponent.GetSomeSpiritVal('fire'))
		self.AddSomeSpiritVal(self, 'earth', opponent.GetSomeSpiritVal('earth'))
		
class CProtagonist(CCreature):
	'''
	主人公类定义
	'''
	def __init__(self):
		super(CProtagonist, self).healthValue = 3
		
		# 拥有五灵珠的情况
		# 集齐金木水火土五灵珠,则直接通关成功
		self.hasBead = {
			"metal": 0,
			"wood" : 0,
			"water": 0,
			"fire" : 0,
			"earth": 0
		}
		
	def AddSomeSpiritVal(self, spiritName, val):
		CCreature(self).AddSomeSpiritVal(spiritName, val)
		print u"恭喜你。你的五灵值升级了，目前为"
		self.PrintSomeSpiritVal()
	def ReduceSomeSpiritVal(self, spiritName, val):
		super(CScene, self).ReduceSomeSpiritVal(spiritName, val)
		print u"很抱歉。你的五灵值降低了，目前为"
		self.PrintSomeSpiritVal()
	def GainSpiritBead(self, spiritName):
		print u"获得%s灵珠" % combat.MapSpiritName[spiritName]
		self.hasBead[spiritName] = 1
		AddSomeSpiritVal(self, spiritName, 1)
		

# 主人公全局对象-张大凡
zhurengong = CProtagonist();


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

