import sys
class Dog:
	pass

dog = Dog()
# 获取引用的个数，调用函数会增加一个引用，所以
# 得到的结果会加1
count = sys.getrefcount(dog)
print(count)
dog2 = dog
count = sys.getrefcount(dog)
print(count)

