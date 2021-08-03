# -*- coding:utf-8 -*-
from HTMLTestRunner import HTMLTestRunner
import unittest

tests=unittest.defaultTestLoader.discover(r"C:\Users\86180\PycharmProjects\day13",pattern="test*.py")

runner=HTMLTestRunner.HTMLTestRunner(
    title="这是一份计算机的测试报告",
    description="这是运算的测试报告",
    verbosity=1,
    stream=open("计算机.html",mode="w+",encoding="utf-8")


)

runner.run(tests)
