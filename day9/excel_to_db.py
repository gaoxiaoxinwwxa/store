# -*- coding: utf-8 -*-

import xlrd
from DBUtils import insert


def excel_to_mysql():
    wd = xlrd.open_workbook("2020年每个月的销售情况.xlsx", encoding_override=True)  # 打开excel
    n = 0
    while True:
        if n < 12:
            sheet = wd.sheet_by_index(n)
            rows = sheet.nrows  # 所有行
            cols = sheet.ncols  # 所有列
            date_index = 0  # 日期列角标
            name_index = 1  # 服装名称所在的列角标
            price_index = 2  # 价格列角标
            count_index = 3  # 库存量的列角标
            sale_index = 4  # 日销售量的列角标
            for i in range(1, rows):
                date = sheet.cell_value(i, date_index)  # 获取日期
                name = sheet.cell_value(i, name_index)  # 获取服装的名称
                price = float(sheet.cell_value(i, price_index))  # 获取单价
                count = int(sheet.cell_value(i, count_index))  # 获取库存量
                sales = int(sheet.cell_value(i, sale_index))  # 获取日销售量
                sql = 'insert into %s月 values (%s,%s,%s,%s,%s)'
                data = [int(n + 1), date, name, price, count, sales]
                insert(sql, data)
            n = n + 1
        else:
            print('\033[35;1m导入MySQL完成！\033[0m')
            break
