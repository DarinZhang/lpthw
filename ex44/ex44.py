# -*- coding: utf-8 -*-

class Parent(object):
	
	def override(self):
		print "PARENT override()"
	
	def implicit(self):
		print "PARENT implicit()"
	
	def altered(self):
		print "PARENT altered()"
		
class Other(object):
	
	def override(self):
		print "OTHER override()"
		
	def implicit(self):
		print "OTHER implicit()"
		
	def altered(self):
		print "OTHER altered()"

class Child(Parent):
	
	def __init__(self):
		self.other = Other()	
	
	def override(self):
		print "CHILD override()"
		self.other.override()
	
	def altered(self):
		print "CHILD, before PARENT altered()"
		# Parent.altered(self)
		super(Child, self).altered()
		self.other.altered()
		print "CHILD, after PARENT altered()"
		

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()