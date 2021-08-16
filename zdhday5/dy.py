# -*- coding:utf-8 -*-
from appium import webdriver
import time

server = r'http://localhost:4723/wd/hub'      # Appium Server, 端口默认为4723
desired_capabilities = {
    'platformName': 'Android',    # 平台
    'deviceName': '127.0.0.1:62001',
    'platformVersion': '7.1.2',      # 安卓版本
    'appPackage': 'com.ss.android.ugc.aweme',      #APP包名
    'appActivity': 'com.ss.android.ugc.aweme.splash.SplashActivity'       # APP启动名

}
driver = webdriver.Remote(server, desired_capabilities) # 连接手机和APP

def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x, y


x, y = get_size()
time.sleep(3)

while True:
    try:
        driver.swipe(x * 0.5, y * 0.9, x * 0.5, y * 0.2)
        time.sleep(6)
    except:
        print('没有更多')
        driver.close()
        driver.quit()
        break

