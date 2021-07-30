# -*- coding:utf-8 -*-
import pymysql
import random  # 随机数
import os  # 按任意键继续

"""
    账户ID为键
"""


# 银行的库
# names = {
#     10000001: {
#         "username": "test1",
#         "password": "123456",
#         "money": 10000,
#         "country": "中国",
#         "province": "北京",
#         "street": "沙河镇街道",
#         "door": "狼腾测试员",
#         "bank_name": "中国建设银行昌平支行"
#     },
#     10000002: {
#         "username": "test2",
#         "password": "654321",
#         "money": 20000,
#         "country": "中国",
#         "province": "上海",
#         "street": "东方明珠",
#         "door": "001",
#         "bank_name": "中国建设银行东方支行"
#     }
# }

# 开户行名称
class Bank:
    def __init__(self, bank_name="中国建设银行昌平支行", host="localhost", user="root", passwd="", db="hkr"):
        self.__bank_name = bank_name
        self.__host = host
        self.__user = user
        self.__passwd = passwd
        self.__db = db
        self.__wellCome = """
        ------------------------------------
        |      欢迎来到中国建设银行昌平支行    |
        ------------------------------------
        |             1.开户               | 
        |             2.存钱               |
        |             3.取钱               |
        |             4.转账               |
        |             5.查询               |
        |             6.退出               |
        ------------------------------------
"""

    # 银行添加用户
    def bank_add_user(self, username, password, money, country, province, street, door):
        # 1.连接数据库
        con = pymysql.connect(host=self.__host, user=self.__user, passwd=self.__passwd, db=self.__db)
        # 2.创建控制台
        cj = con.cursor()
        # 3.准备一条sql语句    # 用户库已满
        sql = "select id from bank"
        cj.execute(sql)
        tt = cj.fetchall()
        length = len(tt)
        if length >= 100:
            return False

        account = random.randint(10000000, 99999999)
        # 录入
        global bank_name
        # 3.准备一条sql语句
        sql = "insert into  bank values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        param = [account, username, password, money, country, province, street, door, self.__bank_name]
        # 4.执行sql
        cj.execute(sql, param)  # (模板, 参数)
        # 5.提交数据到数据库
        con.commit()  # 提交
        # 6.关闭资源
        cj.close()
        con.close()
        return account

    # 开户
    def add_user(self):
        username = input("请输入账户用户名：")
        password = input("请输入账户密码：")
        money = input("请输入账户金额：")
        if money.isdigit():
            money = int(money)
            country = input("请输入所属国籍：")
            province = input("请输入所属省份：")
            street = input("请输入所属街道：")
            door = input("请输入门牌号：")
            account: int
            status = self.bank_add_user(username, password, money, country, province, street, door)
            if status is False:
                print("开户失败")
            else:
                account = status
                con = pymysql.connect(host=self.__host, user=self.__user, passwd=self.__passwd, db=self.__db)
                cj = con.cursor()
                sql = "select id from bank"
                cj.execute(sql)
                print("开户成功！")
                info = """"
                    ----------个人信息【建设银行】---------
                    账户ID：{account}
                    用户名：{username}
                    密码：{password}
                    金额：{money}
                    居住地址：
                        国籍：{country}
                        省份：{province}
                        街道：{street}
                        门牌号：{door}
                    ------------------------------------
                """
                print(info.format(account=account, username=username, password=password,
                                  money=money, country=country, province=province,
                                  street=street, door=door, bank_name_tmp=self.__bank_name))
        else:
            print("用户库存已达上限！")

    # 存钱
    def bank_add_money(self, account, money):
        con = pymysql.connect(host=self.__host, user=self.__user, passwd=self.__passwd, db=self.__db)
        cj = con.cursor()
        sql = "select id from bank"
        cj.execute(sql)
        tt = cj.fetchone()

        if account == tt[0]:
            sql = "update bank set money = money + {0} where id = {1}".format(money, account)
            cj.execute(sql)
            con.commit()
            return True
        else:
            return False

    def add_money(self):
        while True:
            account = (input("请输入您的账号："))
            if account.isdigit():
                account = int(account)
                while True:
                    money = (input("请输入您的存款金额："))  # 将输入金额转换成int类型
                    if money.isdigit():
                        money = int(money)
                        status = self.bank_add_money(account, money)
                        if status:
                            con = pymysql.connect(host=self.__host, user=self.__user, passwd=self.__passwd, db=self.__db)
                            cur = con.cursor()
                            sql = "select money from bank where id = {0}".format(account)
                            cur.execute(sql)
                            data = cur.fetchone()
                            con.commit()
                            con.close()
                            cur.close()
                            print("恭喜您存款成功！")
                            print("当前余额为：", data[0])
                            return
                        else:
                            print("未找到该用户，存款失败！请重新输入！")
                            self.add_money()
                            return
                    else:
                        print("输入不合法！请重新输入")
            else:
                print("输入不合法！请重新输入")

    # 取钱
    def bank_take_money(self, account1, password1, money1):
        con = pymysql.connect(host=self.__host, user=self.__user, passwd=self.__passwd, db=self.__db)
        cj = con.cursor()
        sql = "select * from bank"
        cj.execute(sql)
        tt = cj.fetchone()

        if account1 == tt[0]:
            if password1 == tt[2]:
                if money1 > tt[3]:
                    print("余额不足")
                else:
                    sql = "update bank set money = money - {0} where id = {1}".format(money1, account1)
                    cj.execute(sql)
                    con.commit()
                    print("恭喜您取款成功！")
                    return True
            else:
                print("您输入的密码不正确！")
        else:
            print("您输入的账号有误，请重新输入！")

    def take_money(self):
        while True:
            account1 = input("请输入您的账号：\n")
            if account1.isdigit():
                account1 = int(account1)
                password1 = input("请输入密码：\n")
                money1 = input('请输入取款金额：\n')
                if money1.isdigit():
                    money1 = int(money1)
                    status = self.bank_take_money(account1, password1, money1)
                    if status:
                        con = pymysql.connect(host=self.__host, user=self.__user, passwd=self.__passwd, db=self.__db)
                        cur = con.cursor()
                        sql = "select money from bank where id = {0}".format(account1)
                        cur.execute(sql)
                        data = cur.fetchone()
                        con.commit()
                        con.close()
                        cur.close()
                        print("当前余额为：", data[0])
                        return
                    else:
                        print("请重新输入！")
                        self.take_money()
                        return
                else:
                    print("输入不合法！请重新输入")
            else:
                print("输入不合法！请重新输入")

    # 转账
    def transfer(self):
        con = pymysql.connect(host=self.__host, user=self.__user, passwd=self.__passwd, db=self.__db)
        cj = con.cursor()
        while True:
            account = input("请输入您的账户ID：")
            if account.isdigit():
                account = int(account)
                sql = "select id, password, money from bank where id = {0}".format(account)
                cj.execute(sql)
                con.commit()
                tt = cj.fetchone()
                if account == tt[0]:
                    while True:
                        password = input("请输入您的密码：")
                        if password == tt[1]:
                            print("登录成功！您当前余额为：", tt[2])
                            while True:
                                payee = input("请输入收款人账户ID：")
                                if payee.isdigit():
                                    payee = int(payee)
                                    if payee == account:
                                        print("收款人不能是自己！请重新输入")
                                    else:
                                        sql = "select id, password, money from bank where id = {0}".format(payee)
                                        cj.execute(sql)
                                        con.commit()
                                        data1 = cj.fetchone()
                                        if data1 != None and payee == data1[0]:
                                            while True:
                                                q = input("请输入转账金额：")
                                                if q.isdigit():
                                                    q = int(q)
                                                    if q > tt[2]:  # 判断余额是否充足
                                                        print("余额不足")
                                                    else:
                                                        sql = "update bank set money = money - {0} where id = {1}".format(
                                                            q, account)
                                                        cj.execute(sql)
                                                        sql = "select money from bank where id = {0}".format(account)
                                                        cj.execute(sql)
                                                        con.commit()
                                                        tmp = cj.fetchone()
                                                        print("转帐成功！您当前余额为：", tmp[0])
                                                        sql = "update bank set money = money + {0} where id = {1}".format(
                                                            q, payee)
                                                        cj.execute(sql)
                                                        con.commit()
                                                        con.close()
                                                        cj.close()
                                                        return
                                                else:
                                                    print("输入不合法！请重新输入")
                                        else:
                                            print("您输入的收款人不存在！请重新输入")
                                else:
                                    print("输入不合法！请重新输入")
                        else:
                            print("您输入的密码有误！请重新输入！")
                else:
                    con.close()
                    cj.close()
                    print("您输入的账户不存在，请重新输入！")
                    self.transfer()
            else:
                print("输入不合法！请重新输入")

    # 查询
    def inquiry(self):
        while True:
            account = input("输入您的账户：")
            if account.isdigit():
                account = int(account)
                con = pymysql.connect(host=self.__host, user=self.__user, passwd=self.__passwd, db=self.__db)
                cur = con.cursor()
                sql = "select * from bank where id = {0}".format(account)
                cur.execute(sql)
                con.commit()
                data = cur.fetchone()
                if data != None and account == data[0]:
                    while True:
                        password = input("输入您的密码：")
                        if password != data[2]:
                            print("您输入的密码错误，请重新输入！")
                        else:
                            print("登陆成功，以下是您的个人信息")
                            info = """
            -----------个人信息---------
            用户ID：%s
            用户名：%s
            密码：%s
            地址信息
                国家：%s
                省份：%s
                街道：%s
                门牌号: %s
            余额：%s
            开户行地址：%s
            ---------------------------
                            """
                            print(info % (
                                data[0], data[1], data[2], data[4], data[5], data[6], data[7], data[3], data[8]))
                            return
                else:
                    print("您输入的账户不存在，请重新输入！")
            else:
                print("输入不合法！请重新输入")

    # 入口程序 由赵瑞完成整合
    def run(self):
        while True:
            print(self.__wellCome)
            choose = input("请输入需求业务编号：")
            if choose == '1':
                self.add_user()  # 开户
            elif choose == '2':
                self.add_money()  # 存钱 由高晓鑫完成
            elif choose == '3':
                self.take_money()  # 取钱 由叶宪胤完成
            elif choose == '4':
                self.transfer()  # 转账
            elif choose == '5':
                self.inquiry()  # 查询 由张冲完成
            elif choose == '6':
                break  # 退出
            else:
                print("输入非法！请重新输入")
            os.system('pause')  # 按任意键继续

bank = Bank()
bank.run()
