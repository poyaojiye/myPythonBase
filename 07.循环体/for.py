

name = "smartsun"
print("对于字符串\"%s\"逐个字符输出："%name)
print("===========")
for tmp in name: 
	if tmp == "s":
		print("跳过字母s")
		continue
	if tmp == "u":
		print("遇到字母u退出循环")
		break
	print(tmp)
print("===========")
