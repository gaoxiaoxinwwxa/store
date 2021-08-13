# -*- coding:utf-8 -*-
from HTMLTestRunner import HTMLTestRunner
import unittest
import os

tests = unittest.defaultTestLoader.discover(os.getcwd(),pattern="Test*.py")

runner = HTMLTestRunner.HTMLTestRunner(
    title="这是一个HKR的测试报告",
    description="这是一个详细登陆的测试报告",
    verbosity=1,
    stream = open(file="ceshi.html", mode="w+", encoding="utf-8")
)


runner.run(tests)














