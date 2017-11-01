

def sum(a,b,*args,**kwargs):
	result = a + b
	for c in args:
		result += c
	print(kwargs)
	#print(len(args)) 
	print(result)
	print("===================")
sum(1,2,3,4,5,6)
sum(1,2,3)
sum(1,2)
sum(1,2,zhangsan=10,lisi=19)
