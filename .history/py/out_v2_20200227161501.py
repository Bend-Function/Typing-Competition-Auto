'''
@Descripttion: 
@version: 
@Author: Bend Function
@Date: 2020-02-27 16:10:37
@LastEditors: Bend Function
@LastEditTime: 2020-02-27 16:14:56
'''
import pyautogui
import pyperclip
import time
time.sleep(2)

with open("w2.txt","r",encoding='utf-8') as f:
    lines = f.readlines()
    # print(line)
    for line in lines:
        print(line)