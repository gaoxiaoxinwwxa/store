# -*- coding:utf-8 -*-
path = input('请输入图片的路径：\n')
picture = (open(file=path, mode="rb")).read()
photo = (open(file="picture.jpg", mode="wb")).write(picture)