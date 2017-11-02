class Dog:
	def __init__(self):
		self.name = "小狗"
		self.__age = 1 # 定义私有属性
	def setAge(self,age):
		self.__age = age
	
	def getAge(self):
		return self.__age

dog = Dog()
dog.setAge(10)
age = dog.getAge()
print(age)
print(dog.name)
print(dog.__age) # 访问私有属性报错
		
