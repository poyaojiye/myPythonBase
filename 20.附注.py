import keyword

print("python的关键字")
print(keyword.kwlist)

str ="\
1. 其他关键字\n\
	assert 2==1,\"2不等于1\"  # 真返回True, 假返回False并抛出异常\n\
	is x is y # 判断指向的id是否相同\n\
	nonlocal 是 大函数内有效的变量，比global范围小，global是全局变量\n\
	nonlocal 牵扯到闭包的问题，又牵扯到装饰器的问题待续\n\
	yield 类似 return 可以返回一个生成器，待续\n"


print("")
print("========================================================================")
print(str)
print("========================================================================")
