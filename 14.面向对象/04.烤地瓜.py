
class Di_Gua:
	# init 方法
	def __init__(self):
		self.status = "生的"
		self.cookedlevel = 0
		self.condiments = []
	def __str__(self):
		str = "已经考了%d分钟，状态：%s\n"%(self.cookedlevel,self.status)
		str += "添加的佐料有：%s"%(self.condiments)
		print(self.condiments)
		return str
	# 烤方法
	def cook(self,cooktime):
		self.cookedlevel += cooktime
		if self.cookedlevel <3:
			self.status = "生的"
		elif self.cookedlevel <5:
			self.status = "半生不熟"
		elif self.cookedlevel <8:
			self.status = "九成熟"
		elif self.cookedlevel <10:
			self.status = "熟了"
		else:
			self.status = "烤糊了"
	
	def addcondiments(self,condiment):
		self.condiments.append(condiment)

digua = Di_Gua()
print(digua)
digua.cook(1)
digua.cook(1)
digua.cook(1)
digua.addcondiments("盐")
digua.cook(1)
digua.cook(1)
print(digua)
digua.cook(1)
digua.cook(1)
digua.addcondiments("孜然")
digua.cook(1)
print(digua)
digua.cook(1)
digua.cook(1)
digua.cook(1)
digua.addcondiments("芥末")
print(digua)
digua.cook(1)
digua.cook(1)
digua.addcondiments("辣椒")
digua.cook(1)
print(digua)
