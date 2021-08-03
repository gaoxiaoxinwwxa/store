# -*- coding:utf-8 -*-
import unittest
from Calc import Calc
class TestCalc(unittest.TestCase):
    def testSubs(self):
        a=20
        b=11
        c=9

        calc=Calc()
        sum=calc.subs(a,b)

        self.assertEqual(c,sum)










