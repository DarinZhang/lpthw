# -*- coding: utf-8 -*-

def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b
	
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b 
	
print "Let's do some math with just functions!"

age = add(30, 5)  # 35
height =subtract(78, 4) # 74
weight = multiply(90, 2) # 180
iq = divide(100, 2) # 50

print "Age: %d, Height: %d, Weight: %d, iQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here  is a puzzle."

# what =35 +  74 - 50 / 2 * 180 = -4391
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
