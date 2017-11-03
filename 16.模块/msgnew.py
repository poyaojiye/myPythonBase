# __all__变量中添加的对象才能在导入该模块后使用，
# 	     没添加的不能使用
__all__ = ["test1","Test"]
def test1():
	print("========test1==========")
def test2():
	print("========test2==========")

num = 2

class Test:
	pass
