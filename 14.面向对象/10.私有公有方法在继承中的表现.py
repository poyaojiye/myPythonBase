class A:
	def __init__(self):
		self.num1 = 0
		self.__num2 = 10
	
	def test1(self):
		print("test1")
	def __test2(self):
		print("test2")
	def test3(self):
		self.test1()
		self.__test2()

class B(A):
	def test4(self):
		self.__test2()
		print(self.__num2)

b = B()

b.test1()
# b.__test2() # 私有方法不能被继承
print(b.num1)
# print(b.__num2) # 私有属性也不能被继承
b.test3() # 可以通过调用父类的公有方法间接调用父类的私有属性和私有方法
# b.test4() # 子类中不能调用父类中的私有方法私有属性
