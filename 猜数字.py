import random


num = int(random.random() * 200)
count = 0
print("猜数字游戏1--200")
gold=2000
while True:
    if gold == 0 :
        print("金币不足，退出游戏")
        break
    gold = gold-200

    guess = int(input("请输入您要猜的数字："))
    count = count + 1
    if num > guess:
        print("小了！剩余",gold,"金币！")
    elif num < guess:
        print("大了！剩余",gold,"金币！")
    else:
        gold = gold+5000
        print("剩余多少金币",gold)
        print("恭喜你，猜中了，您的猜的数字为：",num,"您猜了",count,"次了！获得",gold,"金币")
        wan =input("是否继续游戏？(y/n):")
        if wan =="n":
           print("欢迎下次再玩！")
           break
        num = int(random.random() * 200)
