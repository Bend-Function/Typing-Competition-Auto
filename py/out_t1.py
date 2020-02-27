'''
@Descripttion: 
@version: 
@Author: Bend Function
@Date: 2020-02-27 15:58:47
@LastEditors: Bend Function
@LastEditTime: 2020-02-27 16:34:27
'''
import pyautogui
import pyperclip
import time
time.sleep(2)
pyautogui.typewrite('Hello world!', interval=0.25)
# pyautogui.typewrite('会改变', interval=0.25)




pyperclip.copy('要输入的汉字\n')  # 先复制
pyautogui.hotkey('ctrl', 'v')  # 再粘贴
