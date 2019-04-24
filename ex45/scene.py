# -*- coding: utf-8 -*-

'''
各种场景类的定义

场景包括：
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

class CScene(object):
	'''
	场景基类
	'''	
	def __init__(self):
		for i  in xrange(1, 4):
			print u"场景加载中，少侠请稍候", '...'*i
		print u"场景加载成功\n"
		
		self.nextScene = 'Defeat'
		
	def Enter(self):
		pass
	
	def GetNextScene(self):
		return self.nextScene
	

class CSceneGreenHandsHamlet(CScene):
	'''
	新手村
	'''
	def __init__(self):
		super(CSceneGreenHandsHamlet, self).__init__()
		print u"====十里坡===="
		print u"听说村外十里坡最近经常出现妖怪伤人事件。近几个月，爹娘都会去那附近采药。"
		print u"实在不放心，决定前去一探究竟。若遇上妖怪，则将其诛杀。"
		
	def Enter(self):
		print u"\n天气晴朗，万里无云。十里坡还是如幼时记忆中的一样，绿草如茵，鸟语花香。"
		print u"并不像村民中口所说的不太平。"
		print u"不如四处走走，就当春游了。"
		
		
	
tScene = CSceneGreenHandsHamlet()
tScene.Enter()	
	
	
	
	
	



