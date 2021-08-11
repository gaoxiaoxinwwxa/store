# -*- coding:utf-8 -*-
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get(r"C:\Users\86180\Desktop\学习文件\pyth自动化\day01\练习的html\练习的html\跳转页面\pop.html")
driver.maximize_window()
driver.find_element_by_id("goo").click()
date=driver.window_handles
driver.switch_to.window(date[1])
driver.find_element_by_id("kw").send_keys("狼腾测试员")
driver.find_element_by_id("su").click()
time.sleep(5)
driver.quit()