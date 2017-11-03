from distutils.core import setup
"""这种注释不能写在函数调用中，让函数以为引号中是参数"""
setup(
	name = "msgTest", # 上传到网站后将显示在网页上的模块名字
    	version = "0.01",
    	py_modules = ["msgTest.sendmsg","msgTest.recmsg"],
    	author = "smart", 
    	author_email = "smart.sun@outlook.com",
    	url = "https://poyaojiye.com",
    	description = "This is just a module deploy demo. ", # 将会显示在网页上的模块描述文字，此描述应精炼易懂
    )
