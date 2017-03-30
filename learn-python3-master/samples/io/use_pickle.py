#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle

d = dict(name='Bob', age=20, score=88)
data = pickle.dumps(d)
print(data)

reborn = pickle.loads(data)
print(reborn)
# 只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系
