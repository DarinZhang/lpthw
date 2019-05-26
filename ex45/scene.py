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
'''

import time
import combat
import figure
from figure import zhurengong as zhangdafan


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
	time.sleep(1)

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
	
class CScStart(CScene):
	'''
	开篇
	'''
	def __init__(self):
		pass
		
	def Background(self):
		# CScene(self).__init__() # Error
		CScene.__init__(self)
		
	def Enter(self):
		self.Background()
		
		# zhangdafan是全局对象，将生命值、五灵值、朱灵珠恢复默认值
		# 否则第二次游戏时，会使用第一次游戏结束时的任务状态
		zhangdafan.__init__()
		
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
		DelaySleep()
		print u"!!!你希望书名是："
		DelaySleep()
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
			
		print u"\n张大凡捡起珠子。"
		DelaySleep()
		print u"!!!你希望珠子颜色是："
		DelaySleep()
		print u"1. 金色"
		print u"2. 绿色"
		print u"3. 蓝色"
		print u"4. 红色"
		print u"5. 黄色"
		beadColor = raw_input("> ")
		
		if beadColor == '1':
			zhangdafan.GainSpiritBead('metal')
		elif beadColor == '2':
			zhangdafan.GainSpiritBead('wood')
		elif '3' == beadColor:
			zhangdafan.GainSpiritBead('water')
		elif beadColor == '4':
			zhangdafan.GainSpiritBead('fire')
		else:
			zhangdafan.GainSpiritBead('earth')		
		
		print u"\n这个人为什么会倒在村口呢？身上的剑伤哪来的？一系列的疑问萦绕在张大凡心头。"
		DelaySleep()
		print u"出于好心，张大凡给他入土为安，给他立了无名碑。"
		DelaySleep()
		# 下一场景:十里坡（练级）
		self.nextScene = 'GreenHandsHamlet'

class CScGreenHandsHamlet(CScene):
	'''
	 十里坡（新手村）
	'''
	def __init__(self):
		pass
	
	def Background(self):
		super(CScGreenHandsHamlet, self).__init__()
		print u"\n\n****半个月后****"
		print u"听说村外十里坡最近经常出现妖怪伤人事件。近几个月，爹娘都会去那附近采药。"
		DelaySleep()
		print u"实在不放心，决定前去一探究竟。"
		DelaySleep()
		
	def Enter(self):
		# Background(self) # Error
		self.Background()
		
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
			print u"妖兽[%d] 即将进入战斗系统" % (i+1)
			DelaySleep()
			res = combat.Combating(monster)
			
			if res == 'win':
				# 对方的五灵值归自己所有
				zhangdafan.AddSpiritForWin(monster)
			elif res == 'defeat':
				# 生命值减一
				zhangdafan.ReduceHealthVal(1)
				if False == zhangdafan.IsAlive():
					# 生命值空了，下一场景：通关失败(死亡)
					self.nextScene = 'Defeat'
					return
		
		combat.CombatReport()		
		print u"\n妖兽几乎都被诛杀。其中一只妖兽躺在地上，奄奄一息，快断气前说道："
		DelaySleep()
		print u"风波店中的天行刀主是你什么人？你为什么会他的武功道法？哼，别得意，我们鬼面门不会放过"
		DelaySleep()
		print u"天玄宗的，你们都等死吧！！！"
		DelaySleep()
		print u"说完，那只妖兽便断气了。\n\n"
		DelaySleep()
		print u"天行刀主？鬼面门？天玄宗？张大凡一时间不知道这些是什么。带着疑虑，张大凡把孩子送回了家。"
		# 下一场景：风波店（卷入江湖追杀）
		self.nextScene = 'DisturbanceShop'
			
class CScDisturbanceShop(CScene):
	'''
	风波店（卷入江湖追杀）
	'''
	def __init__(self):
		pass
	
	def Background(self):
		DelaySleep()
		print u"\n\n夜深人静，窗外星光点点，蛙声一片。"
		DelaySleep()
		print u"张大凡躺在窗口，怎么都睡不着。白天的事情始终没搞清楚。"
		DelaySleep()
		print u"听村里说书先生说过，天玄宗是中原大陆上第一修仙门派，天行刀主是天玄宗的三元老之一。"
		DelaySleep()
		print u"而鬼面门则是第一魔教，门中包括修炼魔功的魔人，及各类妖魔。"
		DelaySleep()
		print u"听说，天行刀主常穿黑衣，脸上有一处刀疤。难道半个月前，在村口遇到的黑衣人就是天行刀主？"
		DelaySleep()
		print u"到底什么人能杀死天行刀主？从妖兽的话里可以推断出，鬼面门意图对付天玄宗。显然，鬼面门已经开始行动。"
		DelaySleep()
		print u"鬼面门究竟有什么阴谋？要怎么对付天玄宗？"
		DelaySleep()
		print u"好多问题困扰着张大凡。看来只能去一趟妖兽提到的风波店，看看能不能发现什么蛛丝马迹。"
		DelaySleep()
		
	def Enter(self):
		# Background(self) # Error
		self.Background()
	
		print u"\n====风波店====\n"
		DelaySleep()
		print u"张大凡住在风波店天字七号房已经三天了，没见到什么奇怪的人或事，跟普通的旅店一样普通。"
		DelaySleep()
		print u"这天晚上不知道吃了什么一直闹肚子，一直往茅厕跑。"
		DelaySleep()
		print u"这不肚子又闹腾了，张大凡蹲茅坑呢。"
		DelaySleep()
		print u"隐隐约约觉得有人在讲话，声音很小，不注意都听不到。"
		DelaySleep()
		print u"张大凡意识到是有人在隔壁某个蹲位窃窃私语，顿时运起真气，屏气聆听。"
		DelaySleep()
		print u"老者：把这个放入天字二号房内香炉内。"
		DelaySleep()
		print u"年轻男子：是。"
		DelaySleep()
		print u"老者：待那人在房内饮完酒后，便会七窍流血而死，进入房间把他包裹内的灵珠拿来给我。"
		DelaySleep()
		print u"年轻男子：遵命。"
		DelaySleep()
		print u"老者：去吧。"
		DelaySleep()
		print u"......"
		DelaySleep()
		print u"对话的俩人是什么人？听他俩的对话似乎要谋杀某个人。不管怎么样，杀人总是不好的。"
		DelaySleep()
		print u"赶紧前往天字二号房通知那位客官。"
		DelaySleep()
		print u"张大凡匆忙从茅厕飞奔至天字二号房，刚近房门，就闻到一丝淡淡的檀香味。"
		DelaySleep()
		print u"此时也顾不得什么礼数了。张大凡撞开房门，看见一穿着华贵丝质衫，头顶玉冠的中年男子"
		DelaySleep()
		print u"正在饮酒。似乎已经喝了几口。（^-^剧情需要，檀香配酒能毒死人。其实不是的，大家别当真。）"
		DelaySleep()
		print u"张大凡：兄台，不可饮酒。不然可能会七窍流血而死。"
		DelaySleep()
		print u"中年男子：-、-、我已饮了数杯，并无大碍。你是何人？为何闯入我房中？"
		DelaySleep()
		print u"张大凡：我无意中得知有人要毒害你，故想来救你。"
		DelaySleep()
		print u"\n说话间，店小二拿着水壶上来问需不要添水。谈话的两人竟然没有听到小二上楼的声响。"
		DelaySleep()
		print u"要知道，房内的中年男子可是天玄宗宗主坐下第一大弟子唐莲。"
		DelaySleep()
		print u"凭他的功力，百步之外的动静能分辨得一清二楚。唐莲心想，这个小二有问题。"
		DelaySleep()
		print u"难道真的像这位小哥说的，有人想毒害他？"
		DelaySleep()
		print u"思虑间，竟觉得胸口气血一阵翻腾，吐了一口老血出来，意识到自己真的中毒了。"
		DelaySleep()
		print u"瞬间，唐莲打出一记碎空拳。拳气直逼店小二命门，小二躲闪不及，一命呜呼。"
		DelaySleep()
		print u"唐莲毒发，神识还有一丝清醒。躺在地上，叫唤着张大凡。"
		DelaySleep()
		print u"刚才的打斗发生的太快。张大凡吓傻了。听到呼唤声，赶紧上前扶起唐莲。"
		DelaySleep()
		print u"一接触到张大凡，唐莲就感应到了张大凡身上有天玄宗天行刀主的功法。看来他是可靠之人。"
		DelaySleep()
		print u"唐莲：我快不行了。我的包袱里有一颗灵珠。你带着它，把它交给我师父天玄宗金光宗主。"
		DelaySleep()
		print u"唐莲：并告诉我师父，鬼面门设计阴谋，欲在八月十五的少林寺英雄大会歼灭各大派。"
		DelaySleep()
		print u"说完，唐莲就断气了。张大凡在他床上找到包袱，胡乱摸了一通，真的摸到一颗珠子。"
		DelaySleep()
		spiritName = zhangdafan.FindNotHasSpBead()
		print u"拿起来一看是%s灵珠" % combat.MapSpiritName[spiritName]
		zhangdafan.GainSpiritBead(spiritName)
		print u"\n躺在地方的小二竟然还有一丝气息，他向窗外发了一记信号烟弹。"
		DelaySleep()
		print u"张大凡心想不妙，这风波店内肯定还有他的不少同党。"
		DelaySleep()
		print u"思考间，就听到门外熙熙攘攘的脚步声。看来只能跳窗而逃了。"
		DelaySleep()
		print u"张大凡跳窗后，一直跑，不敢停歇。他知道身后有一群人在追杀他。"
		DelaySleep()
		print u"跑了数十公里后，发现前面是一处断崖，无处可走了。"
		DelaySleep()
		print u"身后的那群追杀者也赶上来了，一个个都带着鬼面具，其中一个还带着人骨帽，十分可怖。"
		DelaySleep()
		print u"张大凡心想横竖都是死，直接跳了断崖。"
		# 下一场景：东海死火山（奇遇练得神功）
		self.nextScene = "ExtinctVolcanoInEastChinaSea"
		
class CScExVolcanoInEastChinaSea(CScene):
	'''
	东海死火山（奇遇练得神功）
	'''
	def __init__(self):
		pass
	
	def Background(self):
		print u"\n\n三日后，张大凡在海边醒来。"
		DelaySleep()
		print u"头好疼，这是哪里？是地狱吗？因为张大凡记得最后自己跳了悬崖。"
		DelaySleep()
		print u"现在是午夜时分，空中繁星点点。远处还有海浪声传来。"
		DelaySleep()
		print u"看来自己命大，断崖下就是海边。"
		DelaySleep()
		print u"不远处，有个洞口，张大凡艰难地走了过去，想进去避避风浪。"
	
	def Enter(self):
		self.Background()
		
		print u"\n===== 东海死火山 =====\n"
		DelaySleep()
		print u"张大凡进入洞内，发现这洞内有乾坤。"
		DelaySleep()
		print u"洞深处有只凶兽，旁边还有一堆人骨，看来这只凶兽吃了不少人。"
		DelaySleep()
		print u"上前跟它打声招呼？还是避开它，自己躲在一角休息？ 休息[Y] 打招呼[N]"
		res = raw_input("> ")
		
		if res == 'N':
			print u"\n张大凡：兽兽，你好？Hello? Bonjour?"
			DelaySleep()
			print u"五灵兽：哭了。三百年过去了，终于又看到人了。呜呜~~~~"
			DelaySleep()
			print u"张大凡：你不会吃我吧？"
			DelaySleep()
			print u"五灵兽：我可是道家仙兽--五灵兽，不是什么邪魔，怎么会乱吃人？"
			DelaySleep()
			print u"张大凡：那这些白骨？？"
			DelaySleep()
			print u"五灵兽：他们是我五百年前的主人仙灵道长及弟子们的尸骨。自然死亡而已。"
			DelaySleep()
			print u"五灵兽：还有一些是恶徒，想抢夺我看守的宝物，被我诛杀。"
			DelaySleep()
			print u"五灵兽：你我有缘，你若能答出我出的题目，我就把宝物赠与你。"
			DelaySleep()
			print u"五灵兽：题目：背出圆周率，精确到小数点第10位即可"
			resPai = raw_input("> ")
			
			if 0 == resPai.find('3.1415926535'):
				print u"\n五灵兽：看来真是道家有缘人。宝物就赠与你吧。"
				DelaySleep()
				print u"---- 获得 天香续命丹*5 ----"
				print u"恭喜你，生命值+5"
				zhangdafan.AddHealthVal(5)
				spiritName = zhangdafan.FindNotHasSpBead()
				print u"---- 获得 %s灵珠*1----" % combat.MapSpiritName[spiritName]
				zhangdafan.GainSpiritBead(spiritName)				
				spiritName = zhangdafan.FindNotHasSpBead()
				print u"---- 获得 %s灵珠*1----" % combat.MapSpiritName[spiritName]
				zhangdafan.GainSpiritBead(spiritName)
			else:
				print u"\n回答错误，错失宝物。"
			
			DelaySleep()
			print u"\n五灵兽：送你一本武功秘籍，你闲时看看打发时间吧。"
			DelaySleep()
			print u"张大凡拿起那本破书，书名模糊不清，隐约看到叫《乾坤大罗移》。"
			DelaySleep()
			print u"张大凡坐到角落里，一边休息，一边练习秘籍。"
			DelaySleep()
			DelaySleep()
			print u"\n\n数日后，张大凡身体基本恢复。武功水平也已达到武林一等一高手境界。"
		else:
			print u"\n张大凡走到一边自己休息去了。"
			DelaySleep()
			DelaySleep()
			print u"\n\n数日后，张大凡身体基本恢复。"
		
		print u"\n乔装打扮后，来到风波店附近。天字二号房内整洁如旧，仿佛前几天的事就没发生似的。"
		DelaySleep()
		print u"连续在风波店周围晃了几天，都没发现什么可疑的人和事。"
		DelaySleep()
		print u"看来鬼面门的人已经离开这里了。张大凡心想，赶紧要找到天玄宗的金光宗主。"
		DelaySleep()
		print u"告知他详情并小心防范鬼面门。"
		DelaySleep()
		print u"听说，天玄宗在南方第一大城天启城。那就朝南走吧。"
		
		# 下一场景：修罗院（探寻真相，英雄救美，临危受命）
		self.nextScene = "ShuraGarden"
		
class CScShuraGarden(CScene):
	'''
	修罗院（探寻真相，英雄救美，临危受命）
	'''
	def __init__(self):
		pass
	
	def Background(self):
		print u"\n\n这两天，张大凡运足真气，连续急速往南走了百十公里。"
		DelaySleep()
		print u"这里是迷雾森林，离天启城最多还有半日的路程。"
		DelaySleep()
		print u"实在是太累了，便想倚在树下小憩一下，休息片刻再继续赶路。"
		DelaySleep()
		print u"夕阳西下，落日余晖洒在身上暖暖的，张大凡很快就入睡了。"
		DelaySleep()
		print u"突然，张大凡听到女子的呼救声。"
		DelaySleep()
		print u"赶紧睁眼，竟不想太阳一落山，这迷雾森林一片漆黑，还起了瘴气。"
		DelaySleep()
		print u"张大凡立马运起龟息大法，防止瘴气入侵。"
		DelaySleep()
		print u"张大凡循着声音追去，追了数十米，突然没了声音。"
		DelaySleep()
		print u"但是前面似乎有灯光了。隐约看到树林深处有出宅院。"
		DelaySleep()
		print u"张大凡轻声来到院下，院门紧锁。仔细辨认下，看出院名叫 修罗院。"
		DelaySleep()
		print u"看来女子应该是被虏至这院内了。"
		DelaySleep()
		print u"张大凡运足真气，轻轻一跃，落入院内。"
		
	def Enter(self):
		self.Background()
		
		print u"\n\n==== 修罗院 ===="
		DelaySleep()
		print u"院内一房间烛光摇曳，从窗上看到两个影子在对话。"
		DelaySleep()
		print u"老者：人抓到了吗？"
		DelaySleep()
		print u"年轻男子：已抓到。关在柴房了。"
		DelaySleep()
		print u"老者：注意看管，她可是金光老贼的掌上明珠。后天武林大会上看他如何抉择？要天下，还是要女儿？"
		DelaySleep()
		print u"年轻男子：是。"
		DelaySleep()
		print u"\n\n张大凡在院子转了一圈，发现只有东南角的那件屋子外有人看守，看来刚才被虏的女子就关在那儿。"
		DelaySleep()
		print u"张大凡巧妙引开门口的守卫，偷偷潜进屋子里，看到有个人被捆绑着，嘴子塞着麻布。"
		DelaySleep()
		print u"那女子一看到张大凡走近，便挣扎起来。估计把他当做是匪徒了。"
		DelaySleep()
		print u"张大凡：姑娘莫怕，我和那帮匪徒不是一起的。我是来救你的。"
		DelaySleep()
		print u"张大凡取走她嘴里塞着的麻布。那女子没有大声呼喊。"
		DelaySleep()
		print u"女子：少侠救救我。我是天玄宗金光宗主的女儿千落，被这帮鬼面门的门徒绑架至此。"
		DelaySleep()
		print u"张大凡：千落小姐，可知鬼面门绑架你至此，有何阴谋？"
		DelaySleep()
		print u"金千落：再过两日将在少林寺举办英雄大会，选举新一任的武林盟主。"
		DelaySleep()
		print u"金千落：他们要拿我胁迫我爹将盟主之位传于鬼面门，并在少林寺周围埋伏了大批人马，"
		DelaySleep()
		print u"金千落：想一举消灭各武林正派。"
		DelaySleep()
		print u"张大凡：邪魔歪道，痴心妄想。千落小姐，我先带你出去吧。"
		DelaySleep()
		print u"金千落：那就多谢少侠了。"
		DelaySleep()
		print u"张大凡刚好在秘籍中学会了一门障眼法，将一根木棍幻化成千落小姐的样子，用绳子捆绑起来。"
		DelaySleep()
		print u"还在柴房的米缸里施了醉心蛊。然后带着千落小姐悄悄地御剑离去。"
		DelaySleep()
		print u"\n\n夜空下，皎白月光引人遐想。"
		DelaySleep()
		print u"张大凡御剑术还不熟练。一不小心栽了下去。眼看千落就要脸着地，张大凡硬是一转，自己成了肉垫。"
		DelaySleep()
		print u"金千落是扎扎实实地砸在张大凡身上，是一点伤都没受到。"
		DelaySleep()
		print u"金千落脸红着爬起来。她还是第一次与男子这么近距离接触。"
		DelaySleep()
		print u"金千落：公子，你真好。谢谢你又救了我一次。"
		DelaySleep()
		print u"张大凡：举手之劳，不足挂齿。"
		DelaySleep()
		print u"金千落：你我有缘，我愿赠与一灵珠。前提是你能回答上来我的问题。"
		DelaySleep()
		print u"金千落：题目是：但愿人长久 的下一句是什么？"
		res = raw_input(">  ")
		
		# !!!
		# note:从raw_input()输入的字符编码格式为默认字符编码格式GBK
		#      使用decode()将其转为unicode
		#      u"天下" u表示转码为unicode
		if res.decode("GBK") == u"千里共婵娟":
			DelaySleep()
			print u"\n恭喜你，答对了。"
			spiritName = zhangdafan.FindNotHasSpBead()
			print u"--- 获得%s灵珠*1 ---" % combat.MapSpiritName[spiritName]
			zhangdafan.GainSpiritBead(spiritName)
		else:
			DelaySleep()
			print u"\n抱歉，你答错了。与灵珠无缘。"
		
		print u"\n\n张大凡把金千落御剑送回天玄宗，并且得知金光宗主已带着精锐护队前往少林寺。"
		DelaySleep()
		print u"张大凡匆匆御剑前往少林寺。"
		DelaySleep()
		print u"明天的英雄大会注定险境重重，张大凡心想着一定要阻止鬼面门危害武林的同时，不禁运足真气，"
		DelaySleep()
		print u"全速前进。"
		
		# 下一场景：少林寺（英雄大会，拯救江湖）
		self.nextScene = "ShaolinTemple"
			
class CScShaolinTemple(CScene):
	'''
	少林寺（英雄大会，拯救江湖）
	'''
	def __init__(self):
		pass
	
	def Background(self):
		print u"\n\n嵩山脚下，树荫茂密"
		DelaySleep()
		print u"张大凡乔装成鬼面门的一员门徒混在鬼面门里，悄悄地埋伏在英雄大会会场周围。"
		DelaySleep()
		print u"大会进程一直很顺利，没有什么意外。现在进行到选举武林盟主的最后环节了。"
		DelaySleep()
		print u"就在各派欲推选金光宗主为盟主时，突然天空中乌云密布，邪风四起。"
		DelaySleep()
		print u"忽然有一个人站在会场上。脸色发青，眼窝深邃，眉间一道褐色印记。"
		DelaySleep()
		print u"此人便是鬼面门门主叶鼎天。"
		DelaySleep()
		print u"叶鼎天：我不服。金光老贼你何德何能配得上武林盟主？"
		DelaySleep()
		print u"叶鼎天：还不是仗着你天玄宗人多势众。有本事一决高下如何？"
		DelaySleep()
		print u"金光：本尊前日收服阴世幽泉的天魔兽，内功受损。另择他日再切磋如何？"
		DelaySleep()
		print u"叶鼎天：天生怕死，分明就是不敢一战。就想占着武林盟主之位。"
		DelaySleep()
		print u"叶鼎天：你今日若不战，你女儿就是死路一条。"
		DelaySleep()
		print u"叶鼎天长袖一挥，金千落被捆绑着躺在地上。其实，这是张大凡用幻术变化的。"
		DelaySleep()
		print u"!!!突然东方佛光普照，一个自带光芒的男子从天而降。"
		DelaySleep()
		print u"!!!我们的男主角张大凡闪亮登场啦，噔~噔~~噔~~"
	
	def Enter(self):
		self.Background()
		
		print u"\n\n====== 少林寺 ======"
		DelaySleep()
		print u"张大凡：无耻邪人，金光宗主身受重伤，而你却乘人之危，且以千落小姐性命相逼。"
		DelaySleep()
		print u"张大凡：我还从未见过如此厚颜无耻之徒。"
		DelaySleep()
		print u"叶鼎天：金光老贼真可耻，竟派个黄毛小子来打发我。快出来一战，否则我杀了你女儿。"
		DelaySleep()
		print u"金光欲上前迎战，张大凡拦住了他，并告知请放心，自己能对付叶鼎天。"
		DelaySleep()
		print u"张大凡：魔头莫嚣张，你看看躺在地上的人到底是不是千落小姐？"
		DelaySleep()
		print u"叶鼎天仔细查看，才发现这是幻术变化的假人，心想这小子功力竟如此高深。"
		DelaySleep()
		print u"顿时斗气化马，气剑瞬间射向张大凡。"
		DelaySleep()
		print u"!!!BOSS大决战即将到来!!!"
		DelaySleep()
		print u"\n张大凡立马施展五灵秘术，同时配合身上已有的五灵珠，欲布下五灵佛光阵。"
		DelaySleep()
		print u"只见身上的五灵珠渐渐飞向天空"
		
		if zhangdafan.IsGetAllBeads():
			# 已集齐五颗灵珠，布阵成功
			DelaySleep()
			print u"\n金木水火土五颗灵珠已集齐，且各自归位，布阵成功！！！"
			DelaySleep()
			print u"顿时佛光满天，金刚法相浮现，叶鼎天顶不住佛法高深，即将灰飞烟灭。"
			# 下一场景：通关成功
			self.nextScene = 'Pass'
		else:
			# 尚未集齐五颗灵珠，布阵失败
			DelaySleep()
			print u"\n金木水火土五颗灵珠尚未集齐，布阵失败！"
			DelaySleep()
			print u"张大凡心想,看来只能肉搏了。"
			DelaySleep()
			print u"===== 终决之战 ====="
			DelaySleep()
			print u"!!!击杀魔头叶鼎天"
			DelaySleep()
			monster = figure.CMonster()
			bossDingTian = figure.CBoss()
			print u"BOSS 即将进入战斗系统"
			DelaySleep()
			while bossDingTian.IsAlive() and zhangdafan.IsAlive():
				res = combat.Combating(bossDingTian)
				if res == 'win':
					# BOSS失败时，其五灵值不归自己所有
					# 只是生命值减一
					# zhangdafan.AddSpiritForWin(monster)
					bossDingTian.ReduceHealthVal(1)
					bossDingTian.AddAllSptValues()
				elif res == 'defeat':
					# 生命值减一
					zhangdafan.ReduceHealthVal(1)
					if False == zhangdafan.IsAlive():
						# 生命值空了，下一场景：通关失败(死亡)
						self.nextScene = 'Defeat'
						return
			
			self.nextScene = 'Pass'	
			combat.CombatReport()
			print u"\n叶鼎天被打得魂飞魄散，奄奄一息。"
		
		DelaySleep()
		print u"\n\n叶鼎天：小鬼别得意，我已在少林寺周围布下大量魔兵，你们都得为我陪葬。"
		DelaySleep()
		print u"说罢，使用最后一丝真气向空中发出信号。"
		DelaySleep()
		print u"顿时，天空中乌云密布，大量魔兵涌现，各个凶神恶煞，少林寺危在旦夕。"
		DelaySleep()
		print u"张大凡：黄泉路不好走，我们就不陪你了。你看看你的这些魔兵能成什么气候！"
		DelaySleep()
		print u"说罢，张大凡念起醉心咒，只见魔兵一个个晕倒在地上。因为他们吃了前日被张大凡"
		DelaySleep()
		print u"下了醉心蛊的米。"
		DelaySleep()
		print u"\n\n少林寺危机得以解除，各派都纷纷感激张大凡。还有人说让张大凡当武林盟主。"
		DelaySleep()
		print u"张大凡不喜欢受拘束，直接化作一股青团离开了少林寺。"
		DelaySleep()
		print u"从此张大凡成了武林的传说人物，也再也没人见过他。"
		DelaySleep()

class CScPass(CScene):
	'''
	通关成功
	'''
	def __init__(self):
		pass
	
	def Enter(self):
		print u"\n\n===== 通关成功 ====="
		DelaySleep()
		print u"恭喜少侠通关成功。"
		DelaySleep()
		print u"张大凡与千落小姐情投意合，一同回到余杭镇，改名换姓，拜堂成亲，大隐于市。"
		DelaySleep()
		print u"游戏结束|||"
		
class CScDefeat(CScene):
	'''
	通关失败
	'''
	def __init__(self):
		pass
	
	def Enter(self):
		print u"\n\n===== 通关失败 ====="
		DelaySleep()
		print u"胜败乃兵家常事，少侠看开点吧~~~"
		DelaySleep()
		print u"游戏结束|||"		


