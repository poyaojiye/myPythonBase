

def test(a,b,c=10,*args,**kwargs):
	print(a)
	print(b)
	print(c)
	print(args)
	print(kwargs)

names = ['zhangsan','lisi']
map = {'zhangsan':19,'lisi':20}

test(1,2,3,names,map)
test(1,2,3,*names,**map)
