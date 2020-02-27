'''
@Descripttion: 
@version: 
@Author: Bend Function
@Date: 2020-02-27 15:58:47
@LastEditors: Bend Function
@LastEditTime: 2020-02-27 15:59:08
'''
import pyautogui
import pyperclip
import time
time.sleep()

pyperclip.copy('要输入的汉字')  # 先复制
pyautogui.hotkey('ctrl', 'v')  # 再粘贴