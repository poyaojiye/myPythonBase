
# 定义一个类
# 定义类名
# 定义属性
# 定义方法

class Cat:
	# 属性


	# 方法	
	def eat(self):
		print("猫吃东西")
	def drink(self):
		print("猫喝水")
	def introduce(self):
		print("%s的年龄是%d"%(self.name,self.age))

tom = Cat()
tom.eat()
tom.drink()


tom.name = "汤姆"
tom.age = 19

# 获取属性的第一种方法
print("%s的年龄是%d"%(tom.name,tom.age))
# 获取属性的第二种方法
tom.introduce()

lanmao = Cat()
lanmao.name = "蓝猫"
lanmao.age = 7
lanmao.introduce()
