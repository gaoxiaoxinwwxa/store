# -*- coding:utf-8 -*-
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("https://www.suning.com")
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="searchKeywords"]').send_keys("伊利 安慕希黄桃燕麦200g*10瓶")
driver.find_element_by_xpath('//*[@class="search-btn btn-new"]').click()
driver.find_element_by_xpath('//*[@class="highlight"]').click()
date=driver.window_handles
driver.switch_to.window(date[1])
driver.find_element_by_link_text("加入购物车").click()



time.sleep(5)
driver.quit()