#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
	print('try...')
	r = 10 / 0
	print('result:', r)
except ZeroDivisionError as e:
	print('except:', e)
finally:
	print('finally...')
print('END')
# python的错误其实也是class，所有的错误类型都继承自BaseException，
# 所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。比如：

'''
try:
	foo()
except ValueError as e:
	print('ValueError')
except UnicodeError as e:
	print('UnicodeError')
	'''
	# 第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类，如果有，也被第一个except给捕获了
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')

# 不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了。
# 这样一来，就大大减少了写try...except...finally的麻烦

