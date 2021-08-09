# -*- coding:utf-8 -*-
f =open(file="daoru.jpg",mode="rb")
f1 =open(file="c:\\doo\\daochu.jpg",mode="wb")
data=f.read()
f1.write(data)
f1.flush()
f1.close()
f.close()
