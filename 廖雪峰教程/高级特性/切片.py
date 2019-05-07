# -*- coding: utf-8 -*-
def trim(s):
    if s == '':                 #判断是否为空字符串
        return s
    else:
        while(s[0] == ' '):     #判断首部是否有空格
            s = s[1:]
            if len(s) == 0:     #判断是否只有空格
                return s
        while(s[-1] == ' '):    #判断尾部是否有空格
            s = s[:-2]
        return s
#     start = 0
#     end = len(s)
#     for n in range(end):
#         if s[n] == ' ':
#             pass
#         else:
#             start = n
#             break
#         if n == end:
#             s = ''
#             return s
    
#    for n in range(1, end):
#        if s[-n] == ' ':
#            pass
#        else:
#            end = end - n + 1
#            break
#    s = s[start:end]
#    return s

# 测试:
if trim('hello  ') != 'hello':
    print(trim('hello  '))
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print(trim('  hello'))
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败5!')
elif trim('    ') != '':
    print("'" + trim('    ') + "'")
    print('测试失败6!')
else:
    print('测试成功7!')