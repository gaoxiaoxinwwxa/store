# -*- coding:utf-8 -*-
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("https://www.jd.com")
driver.maximize_window()
driver.find_element_by_link_text("登录").click()
driver.find_element_by_link_text("账户登录").click()
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("18042343256")
driver.find_element_by_xpath('//*[@id="nloginpwd"]').send_keys("1923958341gg")
driver.find_element_by_xpath('//*[@id="loginsubmit"]').click()
time.sleep(5)
driver.find_element_by_link_text("食品").click()
date=driver.window_handles
driver.switch_to.window(date[1])
driver.find_element_by_xpath('//*[@id="key"]').send_keys("海天 酱油 生抽酱油 1.9L 中华老字号")
driver.find_element_by_xpath('//*[@class="button cw-icon"]').click()
driver.find_element_by_link_text("海天 酱油 味极鲜特级生抽 1.6L 中华老字号").click()
time.sleep(3)
driver.switch_to.window(date[-1])
driver.find_element_by_link_text("加入购物车").click()
time.sleep(10)
driver.quit()