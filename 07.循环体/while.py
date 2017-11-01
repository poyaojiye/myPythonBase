count = 2

# 循环的嵌套
print("循环的嵌套")
while count > 0:
	num = 1
	while num <= 10:
		print(num)
		num +=1
	print("第%d次循环"%(3-count))
	count -= 1 
