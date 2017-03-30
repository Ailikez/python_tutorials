#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])
# 写列表生成式时，把要生成的元素x * x放到前面，
# 后面跟for循环，就可以把list创建出来，十分有用，
# 多写几次，很快就可以熟悉这种语法。
# >>> import os # 导入os模块，模块的概念后面讲到
# >>> [d for d in os.listdir('.')] # os.listdir可以列出文件和目录
# ['.emacs.d', '.ssh', '.Trash', 'Adlm', 'Applications', 'Desktop',
#  'Documents', 'Downloads', 'Library', 'Movies', 'Music', 'Pictures',
#  'Public', 'VirtualBox VMs', 'Workspace', 'XCode']