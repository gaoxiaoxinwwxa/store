# coding: utf-8
class cup:
    Height = 0
    volume = 0
    color = ""
    material = ""

    def deposit(self):
        print(self.material, "材质的", self.color, "颜色的杯子在存放液体!")


c = cup()
c.Height = 10
c.volume = 400
c.color = "紫色"
c.material = "水晶"
c.deposit()


class notbook:
    Screen = 0
    price = 0
    cpu = ""
    memory= 0
    standby = ""

    def Typing(self):
        print(self.price, "元的cpu为", self.cpu, "的笔记本电脑打字!")

    def playinggames(self):
        print(self.price, "元的cpu为", self.cpu, "的笔记本电脑打游戏!")

    def watchingvideos(self):
        print(self.price, "元的cpu为", self.cpu, "的笔记本电脑看视频!")


c = notbook()
c.Screen = 14
c.price = 3000
c.cpu = "i5-1035G1"
c.memory= 8
c.standby = "5分钟"
c.Typing()
c.playinggames()
c.watchingvideos()
