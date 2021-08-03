# -*- coding:utf-8 -*-
import unittest
from Calc import Calc
class TestCalc(unittest.TestCase):
    def testMulti(self):
        a=20
        b=10
        c=200

        calc=Calc()
        sum=calc.multi(a,b)

        self.assertEqual(c,sum)