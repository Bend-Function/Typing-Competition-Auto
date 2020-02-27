'''
@Descripttion: 
@version: 
@Author: Bend Function
@Date: 2020-02-27 18:19:31
@LastEditors: Bend Function
@LastEditTime: 2020-02-27 18:19:50
'''
import time
from selenium import webdriver

driver = webdriver.Firefox()

driver.get('https://dazi.kukuw.com/?tdsourcetag=s_pctim_aiomsg')
time.sleep(5)


driver.switch_to.active_element.send_keys(u"龙市唐川")

