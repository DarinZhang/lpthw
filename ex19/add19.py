# -*- coding: utf-8 -*-

def estimate_your_salary_by_age(age):
	if age <= 16:
		print "You are a teenager. Maybe, no salary."
	if age > 16 and age <= 22: 
		print "You are still in school. Maybe, you can work part-time, so your salary may be ￥500"
	if age > 22 and age <= 25:
		print "You could graduate. Maybe your salary is ￥5000"
	if age > 25 and age <= 35:
	    print "Promotion. Maybe your salary is ￥100000"
	if age > 35:
		print "You may become a manager. Maybe your salary is ￥30000"
		
def print_new_line():
	print "\n"


		
#1
estimate_your_salary_by_age(5)
print_new_line()

#2
my_age = 20
estimate_your_salary_by_age(my_age)
print_new_line()

#3
estimate_your_salary_by_age(my_age+10)
print_new_line()

#4
print "Estimate your salary\n"
my_age = raw_input("Please enter you age: ")
estimate_your_salary_by_age(my_age)
print_new_line()

#5 
estimate_your_salary_by_age(28)
print_new_line()

#6
estimate_your_salary_by_age(int(raw_input("Your age: ")))
print_new_line()

#7
fileInfo = open("age.txt")
my_age = fileInfo.read()
estimate_your_salary_by_age(int(my_age))
print_new_line()




