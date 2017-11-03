str= "\
1. 写好一个包后\n\
2. 在包文件夹的同目录下创建setup.py\n\
		from distutils.core import setup\n\
		\"\"\"这种注释不能写在函数调用中，让函数以为引号中是参数\"\"\"\n\
		setup(\n\
			name = \"msgTest\", # 上传到网站后将显示在网页上的模块名字\n\
			version = \"0.01\",\n\
			py_modules = [\"msgTest.sendmsg\",\"msgTest.recmsg\"],\n\
			author = \"smart\", \n\
			author_email = \"smart.sun@outlook.com\",\n\
			url = \"https://poyaojiye.com\",\n\
			description = \"This is just a module deploy demo. \", # 将会显示在网页上的模块描述文字，此描述应精炼易懂    \n\
			)\n\
3. python3 setup.py build\n\
4. python3 setup.py sdist\n\
5. 得到打包好的tar.gz文件\n\
6. 解压文件，进入文件夹\n\
7. sudo python3 setup.py install\n\
8. 怎么卸载安装的python模块\
"

print("")
print("=========================================================================")
print(str)
print("=========================================================================")
