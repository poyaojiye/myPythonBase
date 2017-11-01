
def jiecheng(num):
	if (num -1) == 1:
		result = num * (num - 1)
	else:
		result = num * jiecheng(num -1)	
	return result

num = int(input("请输入要计算阶乘的数字："))
print(jiecheng(num))
