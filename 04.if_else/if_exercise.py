# -*- coding:utf-8  -*-


age = input("请输入你的年龄:")

age = int(age)
# 判断是否能去网吧

if age >= 18 and age <= 100:
	print("你可以去网吧上网啦~~")
	print("你可以去网吧上网啦~~")
	print("你可以去网吧上网啦~~")
	print("你可以去网吧上网啦~~")
	print("你可以去网吧上网啦~~")
elif age < 18: 
	print("你是未成年人，回家找妈妈吧~~")
	print("你是未成年人，回家找妈妈吧~~")
	print("你是未成年人，回家找妈妈吧~~")
	print("你是未成年人，回家找妈妈吧~~")
	print("你是未成年人，回家找妈妈吧~~")
else:
	print("回家养老吧，老头~~")


print("if可以嵌套！！！！")
