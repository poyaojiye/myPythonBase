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
elif age > 100 and age <= 150:
	print("回家养老吧，老头~~")
else:
	pass #占位
	print("pass在python中可以用作临时占位，保证代码的完整性")


print("")
print("========================")
print("if可以嵌套！！！！")
print("在python布尔运算中，如果对象不为空则True,为空则为False;数字0为False，非0返回True")
print("bool([])")
print("bool({})")
print("bool(\"\")")
print("bool(0)")
print("以上均返回False")
print("bool([1])")
print("bool(345)")
print("以上均返回True")
print("在条件语句中按以上规则判断执行")

