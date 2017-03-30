#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 类是创建实例的模板，而实例则是一个一个具体的对象，
# 各个实例拥有的数据都互相独立，互不影响；
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
        '''
        要定义一个方法，除了第一个参数是self外，
        其他和普通函数一样。要调用一个方法，只
        需要在实例变量上直接调用，除了self不用传
        递，其他参数正常传入
        '''
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

print('bart.name =', bart.name)
print('bart.score =', bart.score)
bart.print_score()

print('grade of Bart:', bart.get_grade())
print('grade of Lisa:', lisa.get_grade())
# 千万不要把实例属性和类属性使用相同的名字，
# 因为相同名称的实例属性将屏蔽掉类属性，但是
# 当你删除实例属性后，再使用相同的名称，访问到的将是类属性。