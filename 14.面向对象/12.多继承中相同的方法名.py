class Base:
	def test(self):
		print("=========test==========")

class A(Base):
	def test(self):
		print("=========testA=========")

class B(Base):
	def test(self):
		print("=========testB=========")

class C(A,B):
	pass
	#def test(self):
		#print("=========testC=========")

c = C()
c.test()
# 有个C3算法按照下面的顺序找调用的方法，调用的方法按照下面打出来的顺序查找
# 以后开发的时候尽量不要在同时被继承的类中定义重名的方法
print(C.__mro__)
