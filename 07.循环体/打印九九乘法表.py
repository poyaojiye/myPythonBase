
count = 1

while count <= 9:
	num = 1
	while num <= count:
		print("%d*%d=%d\t"%(num,count,num*count),end="")
		num += 1
	print()
	count += 1
