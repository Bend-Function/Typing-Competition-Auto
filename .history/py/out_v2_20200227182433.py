'''
@Descripttion: 
@version: 
@Author: Bend Function
@Date: 2020-02-27 16:10:37
@LastEditors: Bend Function
@LastEditTime: 2020-02-27 18:24:32
'''
import pyautogui
import pyperclip
import time
# time.sleep(2)

list = []
with open("w2.txt","r",encoding='utf-8') as f:
    lines = f.readlines()
    # print(line)
    for line in lines:
        if line != '':
            list.append(line)

