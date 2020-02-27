'''
@Descripttion: 
@version: 
@Author: Bend Function
@Date: 2020-02-27 18:19:31
@LastEditors: Bend Function
@LastEditTime: 2020-02-27 20:25:41
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
time.sleep(15)


for i in range(0,len(list)):
    driver.switch_to.active_element.send_keys(list[i][0:len(list[i]) - 1])
    for i in range(0,3):
        driver.switch_to.active_element.send_keys(Keys.BACKSPACE)
    driver.switch_to.active_element.send_keys(list[i][len(list[i]-4):len(list[i]-1)])
    time.sleep(3.9)
