#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Animal(object):
	pass


# 大类:
class Mammal(Animal):
	pass


class Bird(Animal):
	pass


# 各种动物:
class Dog(Mammal):
	pass


class Bat(Mammal):
	pass


class Parrot(Bird):
	pass


class Ostrich(Bird):
	pass


'''我们要给动物再加上Runnable和Flyable的功能，只需要先定义好Runnable和Flyable的类：'''


class Runnable(object):
	def run(self):
		print('Running...')


class Flyable(object):
	def fly(self):
		print('Flying...')


'''对于需要Runnable功能的动物，就多继承一个Runnable，例如Dog：'''


class Dog(Mammal, Runnable):
	pass


'''对于需要Flyable功能的动物，就多继承一个Flyable，例如Bat：'''


class Bat(Mammal, Flyable):
	pass


'''通过多重继承，一个子类就可以同时获得多个父类的所有功能。'''

'''MixIn'''
'''
在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。
但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了
继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。
为了更好地看出继承关系，我们把Runnable和Flyable改为RunnableMixIn和FlyableMixIn。
类似的，你还可以定义出肉食动物CarnivorousMixIn和植食动物HerbivoresMixIn，让某个动物同时拥有好几个MixIn：'''


class RunnableMixIn(object):
	def run(self):
		print('Running...')


class FlyableMixIn(object):
	def fly(self):
		print('Flying...')


class CarnivorousMixIn(object):
	def eat(self):
		print('eating meat...')

'''MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，
 我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。'''
class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
	pass


husky = Dog()
husky.eat()
husky.run()
