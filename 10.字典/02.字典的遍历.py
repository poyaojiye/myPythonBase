

map = {'zhangsan':18,'lisi':20,'wangwu':19,'zhaoliu':18}
print(map)
print(map.keys())
print(map.values())
print(map.items())
for m in map.items():
	a,b = m
	print("%s\t%s"%(a,b))
