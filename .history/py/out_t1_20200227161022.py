'''
@Descripttion: 
@version: 
@Author: Bend Function
@Date: 2020-02-27 15:58:47
@LastEditors: Bend Function
@LastEditTime: 2020-02-27 16:10:22
'''
import pyautogui
import pyperclip
import time
time.sleep(2)

pyperclip.copy('要输入的汉字\n')  # 先复制
pyautogui.hotkey('ctrl', 'v')  # 再粘贴
