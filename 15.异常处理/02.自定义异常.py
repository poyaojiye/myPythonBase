class ShortInputException(Exception):
	"""自定义的异常类"""
	def __init__(self, length, atLeast):
		#super().__init__()
		self.lenght = length
		self.atLeast = atLeast

def main():
	try:
		s = input("请输入 --> ")
		if len(s) < 3:
			# raise引发一个你定义的异常
			raise ShortInputException(len(s),3)
	except ShortInputException as result:
		print("ShortInputException:输入的长度是 %d,长度至少应是%d"%(result.length,result.atLeast))
	else:
		print("没有异常发生")

main()

