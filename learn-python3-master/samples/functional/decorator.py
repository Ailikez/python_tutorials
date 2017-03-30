#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 现在，假设我们要增强now()函数的功能，比如，在函数调用
# 前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
# 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：
import functools


def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)

	return wrapper


# 把@log放到now()函数的定义处，相当于执行了语句： now = log(now)
@log
def now():
	print('2015-3-25')


now()


# 和两层嵌套的decorator相比，3层嵌套的效果是这样的：
'''now = log('execute')(now)'''
# 因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator
# 装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'
# 因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__
# 等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
# 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps
# 就是干这个事的，所以，一个完整的decorator的写法如下：
def logger(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)

		return wrapper

	return decorator


@logger('DEBUG')
def today():
	print('2015-3-25')


today()
print(today.__name__)


# 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
#
# 再思考一下能否写出一个@log的decorator，使它既支持：
def log(t):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print(t + 'begin call')
			result = func(*args, **kw)
			print(t + 'end call')
			return result
		return wrapper
	if isinstance(t, str):
		# 此时的调用情况： now = log('字符串')(now)
		# 所以就正常返回decorator就行了，变成decorator(now)
		return decorator

	else:
		# 此时调用情况 now = log(now)
		# t 是个函数，肯定过不了isinstance那一关啊
		# 所以应该直接返回decorator(now),再把t变成空字符串
		# 搞定
		f = t
		t = ''
		return decorator(f)