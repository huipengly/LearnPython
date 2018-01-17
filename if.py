# -*- coding: utf-8 -*-

height = 1.75
weight = 80.5

bmi = weight / pow(height, 2)
if bmi < 18.5:
    status = "过轻"
elif (bmi >= 18.5) and (bmi < 25):
    status = "正常"
elif (bmi >= 25) and (bmi < 28):
	status = "过重"
elif (bmi >= 28) and (bmi < 32):
	status = "肥胖"
elif bmi > 32:
	status = "严重肥胖"

print("bmi指数为%.2f， 属于%s" % (bmi, status))