# -*- coding: utf-8 -*-

# three kinds of methods
# 1. dict style
myStuffDict = {}
myStuffDict['apples'] = 'APPLES'
print myStuffDict['apples']

# 2. module style
import myStuffMod
myStuffMod.apples()
print myStuffMod.tangerine

# 3. class style
class MyStuffCls(object):
	def __init__(self):
		self.tangerine = "I like the way you move"
	def apple(self):
		print "I am a classy apple!"

thing = MyStuffCls()
thing.apple()
print thing.tangerine


class Song(object):
	
	def __init__(self, lyrics, singer = None):
		self.lyrics = lyrics
		self.singer = singer
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
	
	def singer_of_song(self):
		print "The song is singed by ", self.singer
	

happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])
					
bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])
						
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()


Jian_yu_fu_sheng = [u"我愿化身石桥", u"受五百年风吹", u"受五百年日晒", u"但求你从桥上走过"]
song_my = Song(Jian_yu_fu_sheng, u"慕寒")
song_my.singer_of_song()
song_my.sing_me_a_song()