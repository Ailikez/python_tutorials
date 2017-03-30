#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = (x * x for x in range(5))
print(s)
for x in s:
	print(x)


def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1
	return 'done'


f = fib(10)
print('fib(10):', f)
for x in f:
	print(x)

# call generator manually:
g = fib(5)
while 1:
	try:
		x = next(g)
		print('g:', x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break


def triangles():
	'''
	:func: 输出杨辉三角
	:intro:
	:param: none
	:return: none
	'''
	L = [1] # 定义一个初始列表，定义一下就完事了，不会有第二次调用，因为 yield L 和 while 1：
	while 1: # 让函数调用next（）或者用for遍历时，卡在循环体内，
		yield L # yield L 运行到这函数会暂停，直到下一次next(),next之后一直卡在循环体内
		L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1] # 一直都在循环这个过程，只不过用next手动让他循环，因为yield导致中断
n = 0
for t in triangles():
	print(t)
	n = n + 1
	if n == 5:
		break
	    