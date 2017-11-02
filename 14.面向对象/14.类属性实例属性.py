class Tool(object):
	# 类属性
	num = 0
	
	# 方法
	def __init__(self,name):
		self.name = name
		Tool.num += 1

	# 类方法 
	@classmethod
	def set_num(cls):
		cls.num = 100
	
	# 静态方法
	@staticmethod
	def class_desc():
		print("我是静态方法，来告诉你这是一个工具类......")

tool1 = Tool("铁锹")
print(Tool.num)
print(tool1.num)
tool2 = Tool("兵工铲")
print(tool1.num)
print(tool2.num)
print(Tool.num)
tool3 = Tool("军刀")
print(tool1.num)
print(tool2.num)
print(tool3.num) # 通过对象取类属性
print(Tool.num)	# 通过类名取类属性


# 调用类方法
tool = Tool("水桶")
tool.set_num() # 通过对象调用类方法
print(Tool.num)
Tool.set_num() # 通过类名调用类方法
print(Tool.num)

# 调用静态方法
tool.class_desc() # 通过对象调用静态方法
Tool.class_desc() # 通过类名调用静态方法

print("")
print("=========================")
print("类也是对象，类对象")
print("类属性在实例对象中共享")
print("实例属性在实例对象中不共享")
print("")
print("什么场景使用静态方法：")
print("1.与类有关，但与对象无关")
print("2.轻方法，不需要创建对象就可以调用")
print("3.工厂方法，虽然现在还不太理解")
print("=========================")
