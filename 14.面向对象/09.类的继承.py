# 定义动物类
class Animal:

	def eat(self):
		print("动物吃东西.......")	
	def drink(self):
		print("动物喝水.......")	
	def sleep(self):
		print("动物睡觉.......")	
	def run(self):
		print("动物会跑.......")	
	def bark(self):
		print("动物会叫...........")

# 定义狗类继承动物类
# 继承父类的写法 
class Dog(Animal):
	def bark(self):
		print("狗会汪汪叫.........")

# 定义猫类继承动物类
class Cat(Animal):
	def catch(self):
		print("猫会捉老鼠..........")

# 定义哮天犬类继承狗类
class Xiaotq(Dog):
	def fly(self):
		print("哮天犬会飞.........")
	def bark(self):
		print("哮天犬会狂叫...........")
		# 第1种方法，调用父类被重写的方法
		super().bark()

wangcai = Dog()
wangcai.eat() # 调用父类的方法
wangcai.bark() # 调用自己定义的方法
tom = Cat()
tom.run()
tom.catch()
xt = Xiaotq()
xt.fly() # 调用自己定义的方法
xt.bark() # 调用重写后的方法，覆盖了父类的方法
# 第2种方法，被重写后，调用父类的方法
Dog.bark(xt) # 被重写后这样调用父类的方法
# 第2种方法可以调用父类的父类的方法
Animal.bark(xt)

