# -*- coding: utf-8 -*-
def product(*nums):
    if len(nums):
        pro = 1
    else:
        raise TypeError("params must")
    for num in nums:
        pro = pro * num
    return pro
print('product() = ', product())
# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败1!')
elif product(5, 6) != 30:
    print('测试失败2!')
elif product(5, 6, 7) != 210:
    print('测试失败3!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败4!')
else:
    try:
        product()
        print('测试失败5!')
    except TypeError:
        print('测试成功!')