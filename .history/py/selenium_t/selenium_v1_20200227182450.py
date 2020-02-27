'''
@Descripttion: 
@version: 
@Author: Bend Function
@Date: 2020-02-27 18:19:31
@LastEditors: Bend Function
@LastEditTime: 2020-02-27 18:24:50
'''
import time
from selenium import webdriver

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


driver.switch_to.active_element.send_keys("line[0]")
