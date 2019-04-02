# -*- coding: utf-8 -*-

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 thinigs in that list. Let's fix that."

# split(ten_things, ' ')
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	# pop(more_stuff)
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	# append(stuff, next_one)
	stuff.append(next_one)
	print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
# pop(stuff)
print stuff.pop()
# notes
# join() 以字符' '来连接列表中的各元素
# join(' ', stuff)
print ' '.join(stuff) # what? cool!
# list[a, b] 即 [list[a], ..., list[b])
# join('#', stuff[3,5])
print '#'.join(stuff[3:5]) # super stllar!