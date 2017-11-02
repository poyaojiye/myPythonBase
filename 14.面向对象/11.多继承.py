class Base:
	def test(self):
		print("=========test==========")

class A(Base):
	def testA(self):
		print("=========testA=========")

class B(Base):
	def testB(self):
		print("=========testB=========")

class C(A,B):
	def testC(self):
		print("=========testC=========")

c = C()
c.test()
c.testA()
c.testB()
c.testC()
