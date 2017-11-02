class Test(object):
	def __init__(self,switch):
		self.switch = switch
	def calc(self, a, b):
		try:
			return a/b
		except Exception as result:
			if self.switch:
				print("捕获异常开启，异常是：")
				print(result)
			else:
				# 否则抛出异常
				raise




a = Test(True)
a.calc(1,0)


print("================我是华丽的分割线=======================")

a.switch = False
a.calc(1,0)
