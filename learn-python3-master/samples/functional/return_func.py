#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax

	return sum


f = lazy_sum(1, 2, 4, 5, 7, 8, 9)
print(f)
print(f())


# why f1(), f2(), f3() returns 9, 9, 9 rather than 1, 4, 9?
def count():
	fs = []
	for i in range(1, 4):
		def f():
			return i * i

		fs.append(f)
	return fs


f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())


# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，
# 它们所引用的变量i已经变成了3，因此最终结果为9。
# 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
# fix:
def count():
	fs = []

	def f(n):
		def j():
			return n * n

		return j

	for i in range(1, 4):
		fs.append(f(i))
	return fs


f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())
