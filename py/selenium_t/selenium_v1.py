'''
@Descripttion: 
@version: 
@Author: Bend Function
@Date: 2020-02-27 18:19:31
@LastEditors: Bend Function
@LastEditTime: 2020-02-27 21:23:08
'''
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

list = []
# 读比赛内容
with open("w2.txt","r",encoding='utf-8') as f:
    lines = f.readlines()
    # print(line)
    for line in lines:
        # 空行和换行符不计
        if line != '' and line != "\n":
            list.append(line)

# 使用Firefox
driver = webdriver.Firefox()
# 打开比赛网页
# A68X1
driver.get('https://dazi.kukuw.com/?tdsourcetag=s_pctim_aiomsg')
time.sleep(5)


for i in range(0,len(list)):
    # 每次输入 step 个字符
    startIndex = 0
    step = 10
    endIndex = step
    while True:
        if endIndex < len(list[i]):
            driver.switch_to.active_element.send_keys(list[i][startIndex:endIndex])
        else:
            driver.switch_to.active_element.send_keys(list[i][startIndex:len(list[i]) - 2])
            break
        
        startIndex = endIndex
        endIndex += step
        time.sleep(1)
        
    # 一次不要输完,免得换行
    # driver.switch_to.active_element.send_keys(list[i][0:len(list[i]) - 2])
    time.sleep(2)
    # 退3格,刷下退格数
    for k in range(0,3):
        driver.switch_to.active_element.send_keys(Keys.BACKSPACE)
    time.sleep(2)
    # 补完
    driver.switch_to.active_element.send_keys(list[i][len(list[i])-5:len(list[i])])
    time.sleep(1)
    # driver.switch_to.active_element.sendKeys(Keys.RETURN)
    time.sleep(3.9)
