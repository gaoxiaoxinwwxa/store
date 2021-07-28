# -*- coding: utf-8 -*-

from DBUtils import creat_table


def creat_mysql_table():
    for n in range(1, 13):
        sql = "DROP TABLE IF EXISTS `%s月`;"
        sql1 = "CREATE TABLE `%s月` (\
          `date` varchar(10) DEFAULT NULL,\
          `name` varchar(10) DEFAULT NULL,\
          `price` float DEFAULT NULL,\
          `count` int(11) DEFAULT NULL,\
          `sales` int(11) DEFAULT NULL\
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"
        data = [int(n)]
        creat_table(sql, data)
        creat_table(sql1, data)
    print('\033[35;1m创建数据库表完成！\033[35;1m')
