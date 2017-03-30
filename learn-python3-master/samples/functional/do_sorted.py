#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from operator import itemgetter

L = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(L))
print(sorted(L, key=str.lower))

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[1]))
print(sorted(students, key=itemgetter(1), reverse=True))


def by_name(t):
	tmp = []
	tmp.append(t[0])
	return tmp
students_name = sorted(students,key=by_name)
print(students_name)


def by_score(t):
	tmp = []
	tmp.append(t[1])
	return tmp
students_score = sorted(students, key=by_score)
print(students_score)
students_score = sorted(students_score, key = by_score, reverse = 1)
print(students_score)
