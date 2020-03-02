'''
@Descripttion: 
@version: 
@Author: Bend Function
@Date: 2020-03-02 12:15:39
@LastEditors: Bend Function
@LastEditTime: 2020-03-02 15:02:57
'''
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

#config--------------------------------
# 退格率 填百分比
BackPro = 1

# 目标WPM
TgWpm = 200

#config--------------------------------
# 因为有退格,所以补偿些时间
WpmDelay = 55 / TgWpm

# 使用Firefox
driver = webdriver.Firefox()
# 打开比赛网页
# A68X1

driver.get('https://dazi.kukuw.com/')
time.sleep(5)

page_source =  driver.page_source
# 把文章内容按行存入list
list = []
start = 0
# normaly,read 300 lines,you can add it
for id in range(0,300):
    div_s = page_source.find("<div id=\"i_"+str(id)+"\"",start)
    if div_s == -1:
        break 
    # 定位文字文字
    wordStart = page_source.find("<span>",div_s) + 6
    wordEnd = page_source.find("</span>",div_s)
    word = page_source[wordStart:wordEnd]
    start = wordEnd
    list.append(word)

# 主循环
for line in list:
    # 这行要打的字 = line
    for word in line:
        # delay calc with target WPM
        time.sleep(random.uniform(WpmDelay-0.2,WpmDelay+0.2))     # TODO
        driver.switch_to.active_element.send_keys(word)
        
        # 退格控制,最后一个字不退,以防bug
        if random.uniform(0,100) <= BackPro and word != line[len(line)-1]:
            time.sleep(0.05)
            driver.switch_to.active_element.send_keys(Keys.BACKSPACE)
            time.sleep(0.05)
            driver.switch_to.active_element.send_keys(word)
            time.sleep(0.05)
        
        if word == line[len(line)-1]:
            time.sleep(0.05)
            driver.switch_to.active_element.send_keys(Keys.RETURN)
            time.sleep(0.05)
 