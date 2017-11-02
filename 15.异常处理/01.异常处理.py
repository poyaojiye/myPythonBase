try:
	11/0
	open("xxxxx")
	print(name)
# 普通异常处理
#except NameError:
#	print("如果有未定义变量，在这里提示....")
#except FileNotFoundError:
#	print("如果文件没有找到，在这里提示....")

# 第二种方法
except (NameError,FileNotFoundError):
	print("如果未定义变量或文件没有找到，在这里提示....")

# 第三种方法
except Exception as ret:
	print("有其他异常，在这里提示...........")
	print(ret)
else:
	print("没有异常才会执行这里")
finally:
	print("=========finally============")

print("================================")
