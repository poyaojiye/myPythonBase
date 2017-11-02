class Dog:
	def print_self(self):
		print("大家好，我是一只汪星人...........")

class Xtq:
	def print_self(self):
		print("hello,我是会飞的哮天犬..........")

def introduce(tmp):
	tmp.print_self()


dog1 = Dog()
dog2 = Xtq()

introduce(dog1)
introduce(dog2)
print("")
print("")
print("======================")
print("多态: 在定义的时候不知道会执行哪个方法，真正执行的时候根据传入的参数判断怎么执行")
print("======================")
print("python既是面向过程的语言，又是面向对象的语言")
print("面向对象的三要素:封装继承多态")
print("======================")
