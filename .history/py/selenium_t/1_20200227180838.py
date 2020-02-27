'''
@Descripttion: 
@version: 
@Author: Bend Function
@Date: 2020-02-27 16:42:59
@LastEditors: Bend Function
@LastEditTime: 2020-02-27 18:08:37
'''
import time

from selenium import webdriver

driver = webdriver.Firefox()

driver.get('https://dazi.kukuw.com/?tdsourcetag=s_pctim_aiomsg')#（示例中使用百度）
time.sleep(5)

src = driver.page_source
tag_loc = src.find("id=\"i_0\"",0, len(src))
name_loc = src.find("name=",tag_loc, len(src))
name_val = src[name_loc:name_loc+]

driver.find_element_by_id("i_1").send_keys(u"龙市唐川")
# .find_element_by_name("n46d31ed35e9373e2[]")

driver.find_element_by_id("su").click()

time.sleep(5)

driver.find_element_by_id("1").find_element_by_tag_name("a").click()