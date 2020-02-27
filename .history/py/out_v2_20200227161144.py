'''
@Descripttion: 
@version: 
@Author: Bend Function
@Date: 2020-02-27 16:10:37
@LastEditors: Bend Function
@LastEditTime: 2020-02-27 16:11:44
'''
import pyautogui
import pyperclip
import time
time.sleep(2)

with open("w2.txt","r",encoding='utf-8') as f:
    line = f.readline()
    print(line)