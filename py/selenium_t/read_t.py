'''
@Descripttion: 
@version: 
@Author: Bend Function
@Date: 2020-03-01 21:46:45
@LastEditors: Bend Function
@LastEditTime: 2020-03-01 22:02:42
'''
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

driver = webdriver.Firefox()
# 打开比赛网页
# A68X1
# 
driver.get('https://dazi.kukuw.com/?tdsourcetag=s_pctim_aiomsg')
time.sleep(3)

page_source =  driver.page_source
print(page_source)

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
    print(word)