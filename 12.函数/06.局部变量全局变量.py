
time = "10点30"
time2 = "2点"
def get_time():
	global time
	time = "11点30"
	print(time)
	print(time2)
print("如果想在函数中使用全局变量需要使用global声明")
get_time()
print(time)
print(time2)

