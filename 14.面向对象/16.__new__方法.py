class Dog(object):
	def __init__(self):
		print("=========init方法==========")
	def __del__(self):
		print("=========del方法==========")
	def __str__(self):
		print("=========str方法==========")
		return "返回str描述"
	def __new__(cls): # cls 此时指的是Dog类对象
		print(id(cls))
		print("=========new方法==========")
		return object.__new__(cls)


print(id(Dog))
xtq = Dog()
print("创建对象的过程：")
print("1. 调用__new__方法，创建一个对象，返回对象的引用给一个变量")
print("2. 调用__init__方法，把刚才的变量传入")
print("3. 返回对象的引用")
