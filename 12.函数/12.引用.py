
a = 100
b = 100
print(id(a))
print(id(b))
a = 101
print(id(a))
print(id(b))

c = [11,22,33,44]
d = c
c.append('55')
print(id(c))
print(id(d))
print(c)
print(d)

c = [55,66]
print(id(c))
print(id(d))
print(c)
print(d)
