'''
@Descripttion: 
@version: 
@Author: Bend Function
@Date: 2020-02-27 14:54:03
@LastEditors: Bend Function
@LastEditTime: 2020-02-27 15:29:49
'''
import re

with open("src.txt",encoding='utf-8') as f:
    lines = f.read()
    # print(lines)
    print(len(lines))
    # while True:
    va_1 = lines.find("value=",0, len(lines))
    print(lines[va_1+7:va_1+100])
    va_2 = lines.find(""value="",0, len(lines))
        

    

