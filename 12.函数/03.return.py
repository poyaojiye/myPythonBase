def test():
	a = 11
	b = 22
	c = 33
	return [a,b,c]

def test2():
	a = 11
	b = 22
	c = 33
	return (a,b,c)
def test3():
	a = 11
	b = 22
	c = 33
	# 这种形式返回的是元组
	return a,b,c
d = test()
print(d)
print(type(d))

d = test2()
print(d)
print(type(d))

a,b,c = test3()
print("a,b,c=%d,%d,%d"%(a,b,c))
