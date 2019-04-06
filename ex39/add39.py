# -*- coding: utf-8 -*-


def getType(param):
	"""Return the type of the entered param"""
	if 'int' in str(type(param)):
		return 'int'
	elif 'list' in str(type(param)):
		return 'list'
	elif 'dict' in str(type(param)):
		return 'dict'
	elif 'tuple' in str(type(param)):
		return 'tuple'
	else:
		return "Unknown Type"
	
def getTypeNew(param):
	"""Return the type of the entered param"""
	if isinstance(param, int):
		return 'int'
	elif isinstance(param, list):
		return 'list'
	elif isinstance(param, dict):
		return 'dict'
	elif isinstance(param, tuple):
		return 'tuple'
	else:
		return "Unknown Type"

def dump(srcDict):
	assert getType(srcDict) == 'dict', "The param is not a dictionary!"
	return srcDict.copy()
	
def printDict(aDict):
	for k,v in aDict.iteritems():
		print k,'->', v

chineseProvince = {}
chineseProvince['JING'] = "Bei Jing"
chineseProvince['SU'] = 'Jiang Su'
chineseProvince['ZHE'] = 'Zhe Jiang'
chineseProvince['HU'] = "Shang Hai"
chineseProvince['WAN'] = 'An Hui'

# add more provices
chineseProvince['XIANG'] = "Hu Nan"
chineseProvince['E'] = "Hu Bei"

print '-' * 10
printDict(chineseProvince)

newDict = dump(chineseProvince)
print "Copy from chineseProvince"
print '-' * 10
printDict(newDict)

assert chineseProvince.get('GAN'), "Not found province addreviated by 'GAN'"
chineseProvince['GAN'] = 'Gan Su'
