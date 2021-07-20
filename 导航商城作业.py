
def start_B():
    while True:
        c = input("请问是否要购物（y/n）？")
        if c == "y":
            B()
            return
        elif c == "n":
            print("继续旅行，祝您旅行愉快！")
            return
        else:
            print("输入非法，请您重新输入")
def A():
    while True:
        city1 = input("请输入您要去的城市：")
        if city1 in data:
            start_B()
            print_place(data[city1])
            city2 = input("请输入二级城市：")
            if city2 in data[city1]:
                start_B()
                print_place(data[city1][city2])
                city3  = input("请输入三级地区：")
                if city3 in data[city1][city2]:
                    start_B()
                    print_place(data[city1][city2][city3])
                    city4 = input("请输入最终目的地：")
                    if city4 in data[city1][city2][city3]:
                        start_B()
                        print("------------------欢迎下次光临wwxa旅行社！------------------")
                        break
            else:
                print("当前城市不存在，别瞎弄！")
        elif city1 == 'q' or city1 == "Q":
            print("------------------欢迎下次光临wwxa旅行社！------------------")
            break
        else:
            print("当前城市不存在，别瞎弄！")
def B():
    import random

    shop = [
        ["劳力士手表",200000],
        ["Iphone 12X plus",12000],
        ["lenovo PC",6000],
        ["HUA WEI WATCH",1200],
        ["Mac PC",15000],
        ["辣条",2.5],
        ["老干妈",13]
    ]


    money = input("请输入您的余额：")
    money = int(money)
    a = random.randint(1,30)
    zhekou=1
    shiyong=False
    while True:
        tmp = 0
        you = input("是否抽一张优惠券？(y/n):")
        if you == "y":

            guess = a
            if guess == 1 or guess == 3 or guess ==15or guess ==17or guess ==30or guess ==25or guess ==16or guess ==7or guess ==9or guess ==13 :
                print("获得老干妈7折优惠券!")
                zhekou=0.7
                tmp = 1
                break
            elif  guess== 2 or guess == 4 or guess ==5or guess ==6or guess ==8or guess ==10or guess ==11or guess ==12or guess ==14or guess ==18or guess ==19or guess ==20or guess ==21or guess ==22or guess ==23or guess ==24or guess ==26or guess ==27or guess ==28or guess ==29:
                print ("获得联想电脑1折优惠券!")
                zhekou=0.1
                tmp = 1
                break
            else:
                print("输入错误，请重新输入!")
        elif you == "n":
            print("未使用优惠券!")
            break
        else:
            print("输入错误，请重新输入!")
        if tmp == 1:
            break

    mycart = []

    i = 0
    while i <= 20:
        for key, value in enumerate(shop):
            print(key, value)
        chose = input("请输入您想要的商品编号：")
        if chose.isdigit():
            chose = int(chose)
            if chose > 6:
                print("您输入的商品不存在！别瞎弄！")
            else:
                if money < shop[chose][1]:
                    print("对不起，穷鬼，您的钱不够！请到其他超市买东西去！")
                else:
                    if chose == 6 and zhekou == 0.7:
                        mycart.append(shop[chose])
                        money = money - shop[chose][1] * 0.7
                        shiyong=True
                        print("恭喜，成功添加购物车！您的余额还剩￥：", money)
                    elif chose == 2 and zhekou == 0.1:
                        mycart.append(shop[chose])
                        money = money - shop[chose][1] * 0.1
                        shiyong=True
                        print("恭喜，成功添加购物车！您的余额还剩￥：", money)
                    else:
                        mycart.append(shop[chose])
                        money = money - shop[chose][1]
                        print("恭喜，成功添加购物车！您的余额还剩￥：", money)
        elif chose == "q" or chose == "Q":
            print("拜拜了，您嘞！欢迎下次光临！")
            break
        else:
            print("对不起，您输入有误，请重新输入！")
        i = i + 1

    print("以下是您的购物小条，请拿好：")
    for key ,value in  enumerate(mycart):
        print(key,value)
    print("本次余额还剩：￥",money)
    if shiyong:
        if zhekou==0.7:
            print("您已使用老干妈的七折优惠券！")
        elif zhekou==0.1:
            print("您已使用联想电脑一折优惠券!")
    else:
        print("您未使用优惠券!")
data = {
    "北京":{
        "昌平":{
            "十三陵":["十三陵水库","沙河水库"],
            "高校":["北京邮电大学","中央戏剧学院","北京师范大学","华北电力大学","北京航空航天大学"],
            "天通苑":["海底捞","呷哺呷哺"]
        },
        "海淀":{
            "公主坟":["军事博物馆","中华世纪园"],
            "科普场馆":["中国科技馆","北京天文馆"],
            "高校":["北京大学","清华大学"],
            "景区":["北京植物园","香山公园","玉渊潭公园"]
        },
        "朝阳":{
            "龙城":["鸟化石国家地质公园","朝阳南北塔"],
            "双塔":["朝阳凌河公园","朝阳凤凰山"]
        },
        "延庆":{
            "龙庆峡":["龙庆峡景区"]

        }
    },

}
def print_place(choice):
    for i in choice:
        print(i)


for i in data:
    print(i)

A()


