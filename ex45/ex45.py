# -*- coding: utf-8 -*-

'''
练习45:你来制作一个游戏

主要参考仙剑类游戏，闯关探宝打怪升级的模式。
具体设计方案请看文档《仙剑101设计脚本》
如果看不懂或不明白的话，直接运行此脚本，
进入游戏玩下就明白了。

剧情写的太多了，写的好累人。跟写小说似的。
'''

# !!!
# note1:从raw_input()输入的字符编码格式为默认字符编码格式GBK
#       使用decode()将其转为unicode
#       u"天下" u表示转码为unicode
#
# note2:import
#       a : import b
#       c : import a  但是c中并不能调用b模块中的方法
#       即import无法传递。
#       另外，尽量避免模块相互import
#

import scene
scene.LoadTip(u"场景模块导入中", u"场景模块导入成功")

Map = {
	"Start" : scene.CScStart(),
	"GreenHandsHamlet" : scene.CScGreenHandsHamlet(),
	"DisturbanceShop" : scene.CScDisturbanceShop(),
	"ExtinctVolcanoInEastChinaSea": scene.CScExVolcanoInEastChinaSea(),
	"ShuraGarden" : scene.CScShuraGarden(),
	"ShaolinTemple" : scene.CScShaolinTemple(),
	"Pass" : scene.CScPass(),
	"Defeat" : scene.CScDefeat()
}

def StartGame():
	# 开始游戏
	nowScene = Map['Start']
	nowScene.Enter()
	nextSceneName = nowScene.GetNextScene()

	while nextSceneName != "Pass" and nextSceneName != "Defeat":
		nowScene = Map[nextSceneName]
		nowScene.Enter()
		nextSceneName = nowScene.GetNextScene()
	
	nowScene = Map[nextSceneName]
	nowScene.Enter()
	
	print u"\n 游戏已结束，是否重新再来一次？是[Y] 否[N]"
	res = raw_input("> ")
	return res

# main函数。脚本入口处
for i in xrange(1,5) :
	res = StartGame()
	if res == 'N':
		break
	elif i >= 3:
		print u"防沉迷游戏系统提醒您，您本次游戏已花费较长时间，被强制退出游戏。"
		print u"请合理安排游戏时间。下次再见。"
		break
		

