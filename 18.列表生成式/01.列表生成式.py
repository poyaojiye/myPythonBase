# python2中的range是有风险的
print(range(10,20))

# range的用法
a = [i for i in range(10,20)]
print(a)
a = [i for i in range(10,20,2)]
print(a)
a = [i for i in range(10)]
print(a)
a = [i for i in range(10) if i%2 == 0]
print(a)
a = [(i,j) for i in range(3) for j in range(2)]
print(a)
a = [(i,j,k) for i in range(3) for j in range(2) for k in range(2)]
print(a)
