'''
@Descripttion: 
@version: 
@Author: Bend Function
@Date: 2020-02-27 22:27:31
@LastEditors: Bend Function
@LastEditTime: 2020-03-01 22:05:34
'''
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

# 使用Firefox
driver = webdriver.Firefox()
# 打开比赛网页
# A68X1
# 
driver.get('https://dazi.kukuw.com/?tdsourcetag=s_pctim_aiomsg')
time.sleep(15)

page_source =  driver.page_source
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


for i in range(0,len(list)):
    # 如果单句太短就直接输出
    if len(list[i]) < 6:
        driver.switch_to.active_element.send_keys(list[i])
        time.sleep(0.2)
        continue
    

    # 每次输入 step 个字符
    startIndex = 0
    step = random.randint(3,5)
    endIndex = step
    while True:
        if endIndex < len(list[i]) - 2:
            driver.switch_to.active_element.send_keys(list[i][startIndex:endIndex])
        else:
            driver.switch_to.active_element.send_keys(list[i][startIndex:len(list[i]) - 2])
            break
        
        startIndex = endIndex
        endIndex += step
        time.sleep(0.5)
        
    time.sleep(4)
    back_num = random.randint(0,2)
    # 退3格,刷下退格数
    for k in range(0,back_num):
        driver.switch_to.active_element.send_keys(Keys.BACKSPACE)
    time.sleep(0.2)
    # 补完
    driver.switch_to.active_element.send_keys(list[i][len(list[i])-back_num-2:len(list[i])])
    time.sleep(0.4)
    # 回车,可能不需要
    driver.switch_to.active_element.send_keys(Keys.RETURN)
    time.sleep(0.2)
