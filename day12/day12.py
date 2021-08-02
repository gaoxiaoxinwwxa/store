# -*- coding:utf-8 -*-
import threading
import time
store = 0

class Cook(threading.Thread):
    name = ""
    count = 0

    def run(self) -> None:
        global store
        while True:
            if store < 600:
                time.sleep(0.5)
                store += 1
                self.count += 1
                print(self.name,"生产了一个面包，共生产了",self.count,"个，当前库存为：",store,"个")
            else:
                time.sleep(0.5)

class Client(threading.Thread):
    name = ""
    money = 3000

    def run(self) -> None:
        global store
        while True:
            if self.money - 2 >= 0:
                if store > 0:
                    store -= 1
                    self.money -= 2
                    print(self.name,"购买了一个面包，还剩",self.money,"元，当前库存为：",store,"个")
                else:  #
                    time.sleep(1)
            else:
                print("{}没钱了".format(self.name))
                return

cok1 = Cook()
cok2 = Cook()
cok3 = Cook()
cok1.name = "张师傅"
cok2.name = "赵师傅"
cok2.name = "叶师傅"

cet1 = Client()
cet2 = Client()
cet3 = Client()
cet4 = Client()
cet5 = Client()
cet1.name = "赵先生"
cet2.name = "李先生"
cet3.name = "刘先生"
cet4.name = "王先生"
cet5.name = "张先生"

cok1.start()
cok2.start()
cok3.start()
cet1.start()
cet2.start()
cet3.start()
cet4.start()
cet5.start()













