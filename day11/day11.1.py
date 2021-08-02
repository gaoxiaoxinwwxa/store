# -*- coding:utf-8 -*-
class Chef:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def zuo(self):
        print("正在蒸饭...")


class Son(Chef):
    def chao(self):
        print("正在炒菜...")


class Grandson(Son):
    def zuo(self):
        print("蒸饭")

    def chao(self):
        print("炒菜")

class Test:
    r = Grandson("张三", 66)
    name = r.get_name()
    age = r.get_age()
    print("我叫{}， 今年{}岁".format(name, age))
    r.zuo()
    r.chao()