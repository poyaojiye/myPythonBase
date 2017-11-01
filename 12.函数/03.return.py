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
d = test()
print(d)
print(type(d))

d = test2()
print(d)
print(type(d))
