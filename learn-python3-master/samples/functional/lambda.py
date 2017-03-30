#!/usr/bin/env python3
# -*- coding: utf-8 -*-
list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
[1, 4, 9, 16, 25, 36, 49, 64, 81]
# 通过对比可以看出，匿名函数lambda x: x * x实际上就是：
#
# def f(x):
#     return x * x
# 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，
# 匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利
# 用变量来调用该函数
def build(x, y):
    return lambda: x * x + y * y