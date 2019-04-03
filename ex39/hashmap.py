# -*- coding: utf-8 -*-

def new(num_buckets = 256):
	"""Initializes a Map with the given number of buckets."""
	# aMap为列表，列表中一共有num_buckets个元素，每个元素也是列表
	# 即此函数返回一个空的二级列表
	aMap = []
	for i in range(0, num_buckets):
		aMap.append([])
	return aMap

def hash_key(aMap, key):
	"""Given a key this will create a number and then convert it to
	an index for the aMap's buckets."""
	# key哈希得到的整数,再用列表aMap的长度取余数
	# 即此函数返回key对应在aMap中的列表元素的下标
	return hash(key) % len(aMap)

def get_bucket(aMap, key):
	"""Given a key, find the bucket where it would go."""
	# 调用函数hash_key()，获得key在aMap中的列表元素下标
	# 即此函数返回key在aMap中的对应的元素（元素是一个列表）
	bucket_id = hash_key(aMap, key)
	return aMap[bucket_id]

def get_slot(aMap, key, default=None):
	"""
	Returns the index, key, and value of a slot found in a bucket.
	Returns -1, key, and default (None if not set) when not found.
	"""
	# 调用函数get_bucket()，返回key在aMap中的对应的元素（元素是一个列表）
	bucket = get_bucket(aMap, key)
	
	# bucket是一个列表，其元素是二元组
	# enumerate(bucket)的作用是得到一个可迭代的对象
	# 即i表示第i个元素的下标i，kv表示对应第i个元素的内容（即二元组）
	for i, kv in enumerate(bucket):
		# k,v分别表示第i个元素，即二元组，的第一个值和第二个值
		k, v = kv
		# 若key等于k,则返回i,k,v
		if key == k:
			return i, k, v
	
	# 若bucket中没有二元组的第一个值等于key,则返回-1，key, default
	return -1, key, default

def get(aMap, key, default=None):
	"""Gets the value in a bucket for the given key, or the default."""
	# 调用函数get_slot()，获得aMap中相匹配的二元组下标以及二元组内容
	# 此函数返回二元组的第二个值（若没有匹配的二元组，则返回default）
	i, k, v = get_slot(aMap, key)
	return v

def set(aMap, key, value):
	"""Sets the key to the value, replacing any existing value."""
	# bucket为key在aMap中哈希对应的列表元素
	bucket = get_bucket(aMap, key)
	# i,k,v分别为key在bucket中对应二元组元素的下标，对应的二元组的第一个值和第二个值
	i, k, v = get_slot(aMap, key)
	
	# 若下标i大于等于0，表示bucket存在对应key的二元组
	if i >= 0:
		# the key exists, replace it
		# 则将存在的二元组元素更新为新的二元组(key, value)
		bucket[i] = (key, value)
	else:
		# 否则，i<0,表示bucket中不存在对应key的二元组
		# 则将二元组(key,value)添加进列表bucket
		# the key does not, append to create it
		bucket.append((key, value))

def delete(aMap, key):
	"""Deletes the given key from the Map."""
	# 调用get_bucket(),获取key在aMap中哈希对应的列表元素，并赋值给bucket
	bucket = get_bucket(aMap, key)
	
	# 便利列表bucket,i为列表bucket的下标
	for i in xrange(len(bucket)):
		# 获取bucket的第i个二元组，并赋值给k,v
		k, v = bucket[i]
		# 若二元组的第一个值等于key,则将此二元组从bucket中删除
		if key == k:
			del bucket[i]
			break

def list(aMap):
	"""Prints out what's in the Map."""
	# 打印aMap中的所有元素
	for bucket in aMap:
		if bucket:
			for k, v in bucket:
				print k, v
		
def listIter(aMap):
	for i, bucket in enumerate(aMap):
		if bucket:
			for k,v in bucket:
				print i, k, v
	