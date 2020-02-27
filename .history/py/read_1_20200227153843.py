'''
@Descripttion: 
@version: 
@Author: Bend Function
@Date: 2020-02-27 14:54:03
@LastEditors: Bend Function
@LastEditTime: 2020-02-27 15:38:42
'''
import re

list = []

with open("src.txt",encoding='utf-8') as f:
    lines = f.read()
    # print(lines)
    print(len(lines))
    tmp = 0
    while True:
        va_1 = lines.find("value=",tmp, len(lines))
        # print(lines[va_1+7:va_1+100])
        va_2 = lines.find("\"",va_1+7, len(lines))
        # print(lines[va_1+7:va_2])
        list.append(lines[va_1+7:va_2])
        tmp = va_2
        if len(lines) - tmp < 10:
            break
    

with open("w2.txt",'a') as f:
    for l in list:
        f.write(l

    

