
# 定义一个类
# 定义类名
# 定义属性
# 定义方法

class Cat:

	# 属性


	# 初始化对象
	def __init__(self,name,age):
		print("---------hello-------")
		self.name = name
		self.age = age
	# 方法	
	def eat(self):
		print("猫吃东西")
	def drink(self):
		print("猫喝水")
	def introduce(self):
		print("%s的年龄是%d"%(self.name,self.age))

tom = Cat("汤姆",19)
tom.eat()
tom.drink()

# tom.name = "汤姆"
# tom.age = 19

# 获取属性的第一种方法
print("%s的年龄是%d"%(tom.name,tom.age))
# 获取属性的第二种方法
tom.introduce()

lanmao = Cat("蓝猫",7)
# lanmao.name = "蓝猫"
# lanmao.age = 7
lanmao.introduce()
