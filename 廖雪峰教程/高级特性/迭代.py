# -*- coding: utf-8 -*-
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    if L:                   #判断list是否为空，非空则为true
        Lmax = -10e10
        Lmin = 10e10
        for n in L:
            if n > Lmax:
                Lmax = n
            if n < Lmin:
                Lmin = n
        return (Lmin, Lmax)
    else:
        return (None, None)
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败1!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败2!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败3!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败4!')
else:
    print('测试成功!')