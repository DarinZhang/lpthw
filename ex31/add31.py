# -*- coding: utf-8 -*-

def TipEnter():
	return raw_input("> ")

print "Which colour do you like best?"
print "1. Red"
print "2. Yellow"
print "3. Blue"
print "4. Green"
print "5. Other"
color = TipEnter()

if color == '1':
	print "I guess you are a sunny person with enough passion for everything."
	print "Is it right? Y(es) or N(o)"
	response = TipEnter()
	if response == "Y":
		print "Bingo! Thnaks for you response!"
	elif response == "N":
		print "All right. I guess wrong."
	else:
		print "You are so cautious."

elif color == '2':
	print "I guess you are a workaholic, are you? Y(es) or N(o)"
	resp = TipEnter()
	if resp == 'Y':
		print "Haha, me too!"
	else:
		print "I think you maybe change another color."

elif color == "3":
	print "Before doing anything, you must make a solid plan? Y(es) or N(o)"
	resp = TipEnter()
	
elif color == '4':
	print "You are a person with golden mean.^-^"

else:
	print "I can't guess anything."