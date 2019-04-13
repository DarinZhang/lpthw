# -*- coding: utf-8 -*-

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass
	
## is-a
class Dog(Animal):
	
	def __init__(self, name):
		## has-a
		self.name = name
		
## is-a
class Cat(Animal):
	
	def __init__(self, name):
		## has-a
		self.name = name
		
## is-a
class Person(object):
	
	def __init__(self, name):
		## has-a
		self.name = name
		## Person has-a pet of some kind
		self.pet = None
		
	def printName(self):
		print "From class person: ", self.name

## is-a
class Employee(Person):
	
	def __init__(self, name, salary):
		## 调用父类person的__init__()方法。此方式特别应用于多重继承情况
		super(Employee, self).__init__(name)
		## has-a
		self.salary = salary
	
	def printName(self):
		print "From class employee: ", self.name
	
	def printNameFromPar(self):
		# super(Employee, self).printName()
		Person.printName(self)
		
## is-a
class Fish(object):
	pass
	
## is-a
class Salmon(Fish):
	pass
	
## is-a
class Halibut(Fish):
	pass
	
## rover is-a Dog
rover = Dog("Rover")

## is-a
satan = Cat("Satan")

## is-a
mary = Person("Mary")

## has-a
mary.pet = satan

## is-a
frank = Employee("Frank", 120000)

## has-a
frank.pet = rover
## has-a
frank.printName()
## has-a
frank.printNameFromPar()

## is-a
flipper = Fish()

## is-a
crouse = Salmon()

## is-a
harry = Halibut()









