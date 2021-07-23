import xlrd

wd = xlrd.open_workbook("2020年每个月的销售情况.xlsx",encoding_override=True)

g=0
st=wd.sheet_names()
for k in range(12):
    sd=wd.sheet_by_index(k)
    rows=sd.nrows
    cols = sd.ncols
    sum = 0
    for i in range(1,rows):
        x=sd.cell_value(i,2)
        a = sd.cell_value(i,4)
        sum=sum+x*a
    print(k+1,"月的销售总金额为：",round(sum,1))


    g+=sum
print("全年的销售总额：",round(g))

num=0
s_st=wd.sheet_names()
dd={}
for m in s_st:
    sg=wd.sheet_by_name(m)
    rows=sg.nrows
    for l in range(1,rows):
        name=sg.cell_value(l,1)
        price=float(sg.cell_value(l,2))
        num=int(sg.cell_value(l,4))
        if name in dd:
            dd[name][0]+=price*num
            dd[name][1] +=  num
        else:
            eee=[price*num,num]
            dd[name]=eee
for key in dd:
    print(key,"的销售总金额为",round(dd[key][0],1))


sum = 0
for mm in range(0,3):
    su=wd.sheet_by_index(mm)
    rows=su.nrows
    cols = su.ncols

    for i in range(1,rows):
        x=su.cell_value(i,2)
        a = su.cell_value(i,4)
        sum=sum+x*a
print("第一季度的销售占比为：",round(sum/g,3)*100,"%")

sum = 0

for mm in range(4,7):
    su = wd.sheet_by_index(mm)
    rows = su.nrows
    cols = su.ncols

    for i in range(1, rows):
        x = su.cell_value(i, 2)
        a = su.cell_value(i, 4)
        sum = sum+x*a
print("第二季度的销售占比为：", round(sum/g,3)*100,"%")

sum = 0

for mm in range(7,10):
    su = wd.sheet_by_index(mm)
    rows = su.nrows
    cols = su.ncols

    for i in range(1, rows):
        x = su.cell_value(i, 2)
        a = su.cell_value(i, 4)
        sum = sum+x*a
print("第二季度的销售占比为：", round(sum/g,3)*100,"%")

sum = 0

for mm in range(9,12):
    su = wd.sheet_by_index(mm)
    rows = su.nrows
    cols = su.ncols

    for i in range(1, rows):
        x = su.cell_value(i, 2)
        a = su.cell_value(i, 4)
        sum = sum+x*a
print("第二季度的销售占比为：", round(sum/g,3)*100,"%")



date=0
for kk in dd:
    date+=dd[kk][1]

for i in dd:
    deee=dd[i][1]/date
    print(i,"全年销售数量占比：",round(deee,3)*100,"%")










