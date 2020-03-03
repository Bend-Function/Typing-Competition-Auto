'''
@Descripttion: 
@version: 
@Author: Bend Function
@Date: 2020-03-02 12:15:39
@LastEditors: Bend Function
@LastEditTime: 2020-03-03 12:55:54
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import random
import logging
logging.basicConfig(level=logging.WARNING)
#config--------------------------------
# 退格率 填百分比
BackPro = 1

# 目标WPM,中文不宜超过200
CnTgWpm = 180
EnTgWpm = 300

# 在进行退格\换行时的等待时间,默认0.05s
normalDelay = 0.1

# WPM波峰,波谷
speedUp = 50
speedDown = 100
# 波动范围
floatPercent = 0.5
# 曲线生成频率,默认5s
speedFrq = 5
#config--------------------------------
#var------------------------
# 统计中文行与英文行,以及字数
CnLines = 0
EnLines = 0
CnWords = 0
EnWords = 0

# 因为有退格,所以补偿些时间
# WpmDelay = 55 / TgWpm

# 判断句子是否为中文.
# 中文返回1,英文返回0
# s 中只要含中文即返回1
def isCn(Character):
    for i in range(0,len(Character)):
        if Character[i] >= u'\u4e00' and Character[i]<=u'\u9fa5':
            return 100
    if i == len(Character)-1:
        return 0

# 为中文与英文行分配速度
def blockSpeed(numBlocks,type):
    global CnTgWpm,EnTgWpm,speedFrq,speedUp,speedDown,floatPercent
    # 配置目标WPM
    if type == "cn":
        TgWpm = CnTgWpm
    else:
        TgWpm = EnTgWpm

    # 生成阶段曲线
    block = []
    # count = 0
    for blockNum in range(0,numBlocks):       
        # 为了营造波动幅度打的曲线,现在先随机方向
        direction = random.randint(0,1)
        if direction:
            ranSpeed = TgWpm + speedUp - random.randint(0,int(speedUp * floatPercent))
        else:
            ranSpeed = TgWpm - speedDown + random.randint(0,int(speedDown * floatPercent))

        block.append(ranSpeed)
    
    return block

#查看当前剩余时间   秒
def timeLimitNow(page_source):
    startTimeLimit = page_source.find("<li class=\"daojishi_time\">") + 26
    endTimeLimit = page_source.find("</li>",startTimeLimit)
    # 换成秒
    # logging.warning("time %s",page_source[startTimeLimit:endTimeLimit])
    timeLimit = int(page_source[startTimeLimit:endTimeLimit - 3]) * 60 + int(page_source[startTimeLimit + 3:endTimeLimit])
    return timeLimit

# 使用Firefox
driver = webdriver.Firefox()
# 打开比赛网页
# A68X1

driver.get('https://dazi.kukuw.com/')
time.sleep(5)

page_source =  driver.page_source

# 查找设定时间
totalTimeLimit = timeLimitNow(page_source)
totalBlock = int(totalTimeLimit / speedFrq)

# 把文章内容按行存入list
list = []
start = 0
# normaly,read 300 lines,you can add it
for id in range(0,300):
    div_s = page_source.find("<div id=\"i_"+str(id)+"\"",start)
    if div_s == -1:
        break 
    # 定位文字行
    wordStart = page_source.find("<span>",div_s) + 6
    wordEnd = page_source.find("</span>",div_s)
    word = page_source[wordStart:wordEnd]
    start = wordEnd
    
    # 统计中文行与英文行
    if isCn(word):
        CnLines += 1
        CnWords += len(word)
        list.append([word,1])
    else:
        EnLines += 1
        EnWords += len([word,0])
        list.append([word,0])

logging.warning("CnLines = %d",CnLines)
logging.warning("EnLines = %d",EnLines)

# 全部分配 ,可能会与期望WPM有误差
CnBlocks = blockSpeed(totalBlock+10,'cn')
EnBlocks = blockSpeed(totalBlock+10,'en')

logging.warning("CnBlocks = %s",CnBlocks)
logging.warning("EnBlocks = %s",EnBlocks)

# 统计中英文当前输入行
CnWriteNow = 0
EnWriteNow = 0

# 主循环
timeSurplusBefore = totalTimeLimit
for numLines in range(0,len(list)):
    logging.warning("line %d",numLines)
    line = list[numLines][0]

    for word in line:
        page_source =  driver.page_source
        timeSurplusNow = timeLimitNow(page_source)
        if timeSurplusBefore - 5 > timeSurplusNow or timeSurplusBefore == totalTimeLimit:
            if list[numLines][1]:
                delay = 60 / CnBlocks[CnWriteNow]
                CnWriteNow += 1 
            else:
                delay = 60 / EnBlocks[EnWriteNow]
                EnWriteNow += 1
            logging.warning("Change Speed-CN %d EN %d speed %d",CnWriteNow,EnWriteNow,int(delay*60))

            timeSurplusBefore = timeSurplusNow

        # delay calc with target WPM
        # time.sleep(random.uniform(delay-0.1,delay+0.1))     # TODO
        time.sleep(delay)
        driver.switch_to.active_element.send_keys(word)
        
        # 退格控制,最后一个字不退,以防bug
        if random.uniform(0,100) <= BackPro and word != line[len(line)-1]:
            time.sleep(normalDelay)
            driver.switch_to.active_element.send_keys(Keys.BACKSPACE)
            time.sleep(normalDelay)
            # driver.switch_to.active_element.send_keys(Keys.BACKSPACE)
            # time.sleep(normalDelay)
            driver.switch_to.active_element.send_keys(word)
            time.sleep(normalDelay)

        # 最后一个字换行,有些文章不会换行
        if word == line[len(line)-1]:
            time.sleep(normalDelay)
            driver.switch_to.active_element.send_keys(Keys.RETURN)
            time.sleep(normalDelay)

