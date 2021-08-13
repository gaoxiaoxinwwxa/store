# -*- coding:utf-8 -*-
import time
class LoginPage:
    def __init__(self,drive):
        self.driver = drive

    def login(self,username,password):

        self.driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
        self.driver.find_element_by_xpath("//*[@id='password']").send_keys(password)


        self.driver.find_element_by_xpath("//*[@id='submit']").click()
        self.driver.save_screenshot("login1.jpg")
    def get_succes_data(self):
        return self.driver.title

    def get_error_data(self):
        return self.driver.find_element_by_xpath("//*[@id='msg_uname']").text




