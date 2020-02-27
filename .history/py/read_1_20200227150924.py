'''
@Descripttion: 
@version: 
@Author: Bend Function
@Date: 2020-02-27 14:54:03
@LastEditors: Bend Function
@LastEditTime: 2020-02-27 15:09:11
'''
import re

f = open("src.txt",encoding='gbk',errors='ignore')
lines = f.read()
print(lines)
print(type(lines))
f.close()
