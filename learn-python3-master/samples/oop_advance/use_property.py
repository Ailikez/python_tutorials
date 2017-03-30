#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
	@property
	def score(self):
		return self._score # 关于此处为何要写下划线 ------》 self.score不能和装饰器@score重名，显然用self._score更合适

	# 可以检查输入的参数正确与否
	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100!')
		self._score = value


s = Student()
s.score = 60
print('s.score =', s.score)
# ValueError: score must between 0 ~ 100!
# s.score = 9999

class Screen(object):
	@property
	def width(self):
		return self._width
	@width.setter
	def width(self, var):
		if not isinstance(var, (int, float)):
			raise ValueError('MUST be an INTEGER or FLOAT!')
		else:
			self._width = var

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, var):
		if not isinstance(var, (int, float)):
			raise ValueError('MUST be an INTEGER or FLOAT!')
		else:
			self._height = var
	@property
	def resolution(self):
		return self._height * self._width



# test:
s = Screen()
s.width = 1024
s.height = 768
print('width is %s, height is %s.' % (s.width,s.height))
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution