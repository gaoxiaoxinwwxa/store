# -*- coding:utf-8 -*-
import pymysql

host = 'localhost'
user = 'root'
password = ''
database = '统计'

con = pymysql.connect(host=host, user=user, password=password, database=database)
cur = con.cursor()

file = (open('用户数据.txt', 'r+', encoding='utf-8')).readlines()
rows = len((open('用户数据.txt', 'r+', encoding='utf-8')).readlines())
sum = 0
for i in range(rows):
    sql = 'INSERT INTO tongji VALUES (%s,%s,%s)'
    part = file[i].split(",", 2)
    data = [part[0], part[1], part[2]]
    cur.execute(sql, data)
    count = int(part[2])
    sum += count
print(sum)
print('录入完成！')
con.commit()
cur.close()
con.close()