class Single_Instance(object):
	
	__instance = None
	__init_flag = True # 判断是否需要初始化
	
	def __new__(cls,name): # 注意，这里name没有使用也要写上
		if cls.__instance == None:
			cls.__instance = object.__new__(cls)
			return cls.__instance
		else:
			return cls.__instance

	def __init__(self,name):
		if Single_Instance.__init_flag:
			self.name = name
			Single_Instance.__init_flag = False


a = Single_Instance("哮天犬")
print(a.name)

b = Single_Instance("旺财")
print(b.name)

print(id(a))
print(id(b))

print("作为单例模式的模板")


