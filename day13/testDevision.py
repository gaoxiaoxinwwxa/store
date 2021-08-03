# -*- coding:utf-8 -*-
import unittest
from Calc import Calc
class TestCalc(unittest.TestCase):
    def testDevision(self):
        a=20
        b=10
        c=2

        calc=Calc()
        sum=calc.devision(a,b)

        self.assertEqual(c,sum)