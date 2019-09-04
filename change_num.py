#!/usr/bin/env python
# 题目要求：交换a、b两个变量，要求不能用临时变量
import random

def ChangeNum(a, b):
	print("Before change: " + "a = " + str(a) + " b = " + str(b))
	a = a + b
	# a = 8
	b = a - b
	# b = 3
	a = a - b
	# a = 5
	print("After change: " + "a = " + str(a) + " b = " + str(b))

random_list = random.sample(range(-10,10), 2)
a = random_list[0]
b = random_list[1]

ChangeNum(a, b)
