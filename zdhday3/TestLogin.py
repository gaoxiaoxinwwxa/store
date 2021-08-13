# -*- coding:utf-8 -*-
from unittest import TestCase
from selenium import webdriver
from ddt import ddt
from ddt import data
from ddt import unpack
from Initpage import Initpage
from LoginPage import LoginPage
import  time
@ddt
class TestLogin(TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/HKR")
        time.sleep(3)


    def tearDown(self) -> None:
        time.sleep(3)
        self.driver.quit()


    @data(*Initpage.login_success_data)
    def testLoginsuccess(self,testdata):

        username = testdata["username"]
        password = testdata["password"]
        expect = testdata["expect"]

        login = LoginPage(self.driver)
        login.login(username,password)


        result = login.get_succes_data()


        self.assertEqual(expect,result)


    @data(*Initpage.login_pwd_error_data)
    def testLoginerror(self, testdata):

        username = testdata["username"]
        password = testdata["password"]
        expect = testdata["expect"]

        login = LoginPage(self.driver)
        login.login(username, password)


        result = login.get_error_data()

        self.assertEqual(expect, result)















