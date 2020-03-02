'''
@Descripttion: 
@version: 
@Author: Bend Function
@Date: 2020-03-02 12:15:39
@LastEditors: Bend Function
@LastEditTime: 2020-03-02 13:01:25
'''
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

#config--------------------------------
# 退格率 填百分比,>1或=0
BackPro = 1
# 目标WPM
TgWpm = 200

#config--------------
WpmDelay = 60 / TgWpm

# 使用Firefox
driver = webdriver.Firefox()
# 打开比赛网页
# A68X1
# 
driver.get('https://dazi.kukuw.com/?tdsourcetag=s_pctim_aiomsg')
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
    wordStart = page_source.find("<span>",div_s) + 6
    wordEnd = page_source.find("</span>",div_s)
    word = page_source[wordStart:wordEnd]
    start = wordEnd
    list.append(word)

# 主循环
for line in list:
    # 这行要打的字 = line
    # 如果单句太短就直接输出
    if len(line) < 6:
        driver.switch_to.active_element.send_keys(line)
        time.sleep(0.2)
        continue
    

    for word in line:
        # delay calc with target WPM
        time.sleep(random.uniform(WpmDelay-0.1,WpmDelay+0.01))     # TODO
        driver.switch_to.active_element.send_keys(word)
        # time.sleep(random.uniform(WpmDelay-0.01,WpmDelay+0.001))

        if random.randint(0,100) <= BackPro:
            driver.switch_to.active_element.send_keys(Keys.BACKSPACE)
            time.sleep(0.1)
            driver.switch_to.active_element.send_keys(word)
            time.sleep(0.1)
        
        if word == line[len(line)-1]:
            driver.switch_to.active_element.send_keys(Keys.RETURN)
            time.sleep(0.1)
