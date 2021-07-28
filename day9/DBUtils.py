# -*- coding: utf-8 -*-

import pymysql

host = 'localhost'
user = 'root'
password = ''
database = 'fz'


# 创表
def creat_table(sql, data):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cur = con.cursor()
    cur.execute(sql, data)
    con.commit()
    cur.close()
    con.close()


# 增
def insert(sql, data):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cur = con.cursor()
    cur.execute(sql, data)
    con.commit()
    cur.close()
    con.close()


# 删
def delete(sql, data):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cur = con.cursor()
    cur.execute(sql, data)
    con.commit()
    cur.close()
    con.close()


# 改
def update(sql, data):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cur = con.cursor()
    cur.execute(sql, data)
    con.commit()
    cur.close()
    con.close()


# 查
def select(sql, data, model, size):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cur = con.cursor()
    cur.execute(sql, data)
    if model == "all":
        return cur.fetchall()
    elif model == "one":
        return cur.fetchone()
    elif model == "many":
        return cur.fetchmany(size)
    con.commit()
    cur.close()
    con.close()
