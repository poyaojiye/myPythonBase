class Dog:
	
	# 私有方法
	def __bite(self):
		print("-------汪汪~-------") 
	def warn(self,who):
		if who == "陌生人":
			self.__bite()
		else: 
			print("没有陌生人，乖乖啃骨头")
dog = Dog()
# dog.__test1() # 直接调用私有方法报错
dog.warn("陌生人")
dog.warn("熟人")
