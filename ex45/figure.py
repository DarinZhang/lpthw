# -*- coding: utf8 -*-
'''
角色类的定义

角色有：
1. 主人公
2. 反派BOSS
3. 小怪
'''

from random import randint
import combat
from collections import defaultdict

class DZMultiMap(object):
	'''
	实现类似C++中multimap类型（键允许重复）
	'''
	def __init__(self):
		self.keyS = []
		self.valueS = []
	
	def Insert(self, key, value):
		self.keyS.append(key)
		self.valueS.append(value)
		
	def Len(self):
		return len(self.keyS)
		
	def GetKeys(self):
		return self.keyS
	
	def GetValues(self):
		return self.valueS
	
	def GetItem(self, index):
		itemIndex = []
		itemIndex.append(self.keyS[index])
		itemIndex.append(self.valueS[index])
		return itemIndex
	
	def PrintItems(self):
		for i in xrange(0, len(self.keyS)):
			print combat.MapSpiritName[self.keyS[i]], " : ", self.valueS[i]


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
	def ReduceSomeSpiritVal(self, spiritName, val):
		self.fiveSpiritVal[spiritName] -= val
	def PrintSomeSpiritVal(self):
		print u"<<< 金:%d 木:%d 水:%d 火:%d 土:%d" % (self.fiveSpiritVal['metal'], self.fiveSpiritVal['wood'],self.fiveSpiritVal['water'],self.fiveSpiritVal['fire'],self.fiveSpiritVal['earth'])
	
	
	def GetThreeCard(self):
		cards = DZMultiMap()
		
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
			else:
				key = 'earth'
			
			cards.Insert(key, self.GetSomeSpiritVal(key))
			
		return cards
	
	def AddSpiritForWin(self, opponent):
		self.AddSomeSpiritVal('metal', opponent.GetSomeSpiritVal('metal'), False)
		# AddSomeSpiritVal(self, 'wood', opponent.GetSomeSpiritVal('wood')) # Error
		self.AddSomeSpiritVal('wood', opponent.GetSomeSpiritVal('wood'), False)
		self.AddSomeSpiritVal('water', opponent.GetSomeSpiritVal('water'), False)
		self.AddSomeSpiritVal('fire', opponent.GetSomeSpiritVal('fire'), False)
		self.AddSomeSpiritVal('earth', opponent.GetSomeSpiritVal('earth'))
		
class CProtagonist(CCreature):
	'''
	主人公类定义
	'''
	def __init__(self):
		CCreature.__init__(self)
		super(CProtagonist, self).SetHealthVal(3)
		
		# 拥有五灵珠的情况
		# 集齐金木水火土五灵珠,则直接通关成功
		self.hasBead = {
			"metal": 0,
			"wood" : 0,
			"water": 0,
			"fire" : 0,
			"earth": 0
		}
		
	def AddSomeSpiritVal(self, spiritName, val, bPrintTip = True):
		# CCreature(self).AddSomeSpiritVal(spiritName, val) # Error
		CCreature.AddSomeSpiritVal(self, spiritName, val)
		# super(CProtagonist, self).AddSomeSpiritVal(spiritName, val)
		# self.fiveSpiritVal[spiritName] += val
		
		if bPrintTip:
			combat.DelaySleep()
			print u"恭喜你。你的五灵值升级了，目前为"
			combat.DelaySleep()
			self.PrintSomeSpiritVal()
			combat.DelaySleep()
			
	def ReduceSomeSpiritVal(self, spiritName, val):
		super(CScene, self).ReduceSomeSpiritVal(spiritName, val)
		combat.DelaySleep()
		print u"很抱歉。你的五灵值降低了，目前为"
		combat.DelaySleep()
		self.PrintSomeSpiritVal()
		combat.DelaySleep()
		
	def GainSpiritBead(self, spiritName):
		'''
		获得某颗灵珠
		'''
		combat.DelaySleep()
		print u"获得%s灵珠" % combat.MapSpiritName[spiritName]
		self.hasBead[spiritName] = 1
		# AddSomeSpiritVal(self, spiritName, 1) # Error
		combat.DelaySleep()
		self.AddSomeSpiritVal(spiritName, 1)
		combat.DelaySleep()
	def FindNotHasSpBead(self):
		'''
		返回尚未获得的某灵珠属性
		'''
		for i in self.hasBead.iteritems():
			if i[1] == 0:
				return i[0]
	def IsGetAllBeads(self):
		'''
		是否已集齐金木水火土无颗灵珠
		'''
		return (self.hasBead.values() == [1,1,1,1,1])
	def InitSpBeads(self):
		'''
		清空灵珠获取情况
		'''
		self.hasBead = {
			"metal": 0,
			"wood" : 0,
			"water": 0,
			"fire" : 0,
			"earth": 0
		}


# 主人公全局对象-张大凡
zhurengong = CProtagonist();


class CBoss(CCreature):
	'''
	反派BOSS类定义
	'''
	def __init__(self):
		# CCreature(self).healthValue = 3 # Error
		super(CBoss, self).__init__()
		super(CBoss, self).SetHealthVal(3)
	
	def AddAllSptValues(self):
		'''
		当BOSS被杀到只剩最后一滴血时，灵力值全部+1
		'''
		if self.healthValue == 1:
			print u"叶鼎天只剩最后一滴血了，拼死一搏，启用魔道禁咒将五灵值全部增加了。"
			self.fiveSpiritVal['metal'] += 1
			self.fiveSpiritVal['wood'] += 1
			self.fiveSpiritVal['water'] += 1
			self.fiveSpiritVal['fire'] += 1
			self.fiveSpiritVal['earth'] += 1
	

class CMonster(CCreature):
	'''
	小怪类定义
	'''
	pass

