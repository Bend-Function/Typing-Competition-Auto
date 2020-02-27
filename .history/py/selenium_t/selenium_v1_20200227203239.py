'''
@Descripttion: 
@version: 
@Author: Bend Function
@Date: 2020-02-27 18:19:31
@LastEditors: Bend Function
@LastEditTime: 2020-02-27 20:32:38
'''
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

list = []
with open("w2.txt","r",encoding='utf-8') as f:
    lines = f.readlines()
    # print(line)
    for line in lines:
        if line != '':
            list.append(line)


driver = webdriver.Firefox()

driver.get('https://dazi.kukuw.com/?tdsourcetag=s_pctim_aiomsg')
time.sleep(5)


for i in range(0,len(list)):
    driver.switch_to.active_element.send_keys(list[i][0:len(list[i]) - 2])
    time.sleep(2)
    for k in range(0,3):
        driver.switch_to.active_element.send_keys(Keys.BACKSPACE)
    time.sleep(2)
    driver.switch_to.active_element.send_keys(list[i][len(list[i])-5:len(list[i])])
    driver.switch_to.active_element.sendKeys(Keys.RETURN)
    time.sleep(3.9)
