class Dog:
	
	# 定义__del__方法
	def __del__(self):
		print("=========删除对象=========")

dog1 = Dog()
dog2 = dog1

del dog1
del dog2
print("===================")
