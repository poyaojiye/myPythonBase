

# 定义全局变量的列表和字典

names = ['zhangsan','lisi']
map = {'zhangsan':18,'lisi':19}

def test():
	names = ['zhangsan','zhaoliu']
	names.append('wangwu')
	map['wangwu'] = 20
	print(names)
	print(map)
test()

print(names)
print(map)
