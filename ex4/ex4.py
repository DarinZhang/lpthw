#!/usr/bin/env python
# -*- codeing: utf-8 -*-
# coding:gbk


# 汽车100辆
cars = 100
# 每辆车有4.0个座位
space_in_a_car = 4.0
# 驾驶员30名
drivers = 30
# 乘客90名
passengers = 90
# 没有驾驶员的汽车数量
cars_not_driven = cars - drivers
# 有驾驶员的汽车数量
cars_driven = drivers
# 所有汽车的载客人数
carpool_capacity = cars_driven * space_in_a_car
# 每辆汽车的乘客人数
average_passengers_per_car = passengers / cars_driven


# 有100辆汽车可用。
print "There are", cars, "cars available."
# 仅有驾驶员30名可用。
print "There are only", drivers, "drivers available."
# 将有70辆汽车没有人驾驶。
print "There will be", cars_not_driven, "empty cars today."
# 我们能够运输120人。
print "We can transport", carpool_capacity, "people today."
# 我们有90名乘客待共乘汽车。
print "We have", passengers, "to carpool today."
# 我们需要在每辆车上安置3名乘客。
print "We need to put about", average_passengers_per_car, "in each car."
