'''
@Descripttion: 
@version: 
@Author: Bend Function
@Date: 2020-02-27 15:58:47
@LastEditors: Bend Function
@LastEditTime: 2020-02-27 15:58:48
'''
import pyautogui
import pyperclip
 
pyperclip.copy('要输入的汉字')  # 先复制
pyautogui.hotkey('ctrl', 'v')  # 再粘贴要输入的汉字