'''
@Descripttion: 
@version: 
@Author: Bend Function
@Date: 2020-02-27 16:42:59
@LastEditors: Bend Function
@LastEditTime: 2020-02-27 16:42:59
'''
import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('输入网址')#（示例中使用百度）

driver.find_element_by_id("kw").send_keys(u"龙市唐川")

driver.find_element_by_id("su").click()

time.sleep(5)

driver.find_element_by_id("1").find_element_by_tag_name("a").click()