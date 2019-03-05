# -*- coding: utf-8 -*-

from sys import argv


# 推销理财产^-^

script, salary, expense = argv

print "According to the information you entered: "
print "\tyour salary is $%s" % salary
print "\tyour expense monthly is $%s" % expense
print "We can figure out: "

surplus = float(salary) - float(expense)
print "\tyour surplus monthly is $%s" % surplus

if surplus <= 0 :
	print "Warning: please cut down your monthly expense!!!"
else : 
	result = raw_input("Do you want to buy financial products? Y(es) or N(o):")
	if result == 'N' :
		print "Thanks"
	else :
		fund = input("How much money are you willing to put into your portfolio for this month?")
		interestRate = 0.06
		print "According the average interest rate of money fund is %.3f" % interestRate
		print "If you insist it for 12 months, it can be estimated out: "
		monthNum = 12		
		fundTotal = fund * ( (1.0+interestRate)**monthNum )
		benefitTotal = fundTotal - fund
		benefitMonth = benefitTotal / float(monthNum)		
		print "\t you can get the average benifit $%5.3f monthly" % benefitMonth
		print "\t and totally %5.3f for one year!!!!!" % benefitTotal
		
		
	
