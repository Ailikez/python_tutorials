#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
    pass

class Dog(Animal):
    pass

class Husky(Dog):
    pass

a = Animal()
d = Dog()
h = Husky()

print('check a = Animal()...')
print('isinstance(a, Animal) =', isinstance(a, Animal))
print('isinstance(a, Dog) =', isinstance(a, Dog))
print('isinstance(a, Husky) =', isinstance(a, Husky))

print('check d = Dog()...')
print('isinstance(d, Animal) =', isinstance(d, Animal))
print('isinstance(d, Dog) =', isinstance(d, Dog))
print('isinstance(d, Husky) =', isinstance(d, Husky))

print('check h = Husky()...')
print('isinstance(h, Animal) =', isinstance(h, Animal))
print('isinstance(h, Dog) =', isinstance(h, Dog))
print('isinstance(h, Husky) =', isinstance(h, Husky))
# 比如下面的代码就可以判断是否是list或者tuple：
# >>> isinstance([1, 2, 3], (list, tuple))
# True
# >>> isinstance((1, 2, 3), (list, tuple))
# True
# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
# 在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，
# 它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：

# >>> len('ABC')
# 3
# >>> 'ABC'.__len__()
# 3