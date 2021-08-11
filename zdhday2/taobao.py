# -*- coding:utf-8 -*-
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("https://login.taobao.com")
driver.maximize_window()

driver.find_element_by_xpath("//*[@id='fm-login-id']").send_keys("18746497823")
driver.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys("1923958341gg")
driver.find_element_by_xpath('//*[@fm-button fm-submit password-login"]').click()
time.sleep(5)
driver.find_element_by_link_text("无线耳机").click()
date=driver.window_handles
driver.switch_to.window(date[1])
driver.find_element_by_link_text("真无线蓝牙耳机双耳运动型入耳式高音质高端2021年新款男女士款降噪高颜值征骑兵tws适用于苹果vivo华为oppo").click()
time.sleep(3)
# driver.switch_to.window(date[-1])
# driver.find_element_by_link_text("加入购物车").click()
time.sleep(5)
driver.quit()