#!/usr/bin/env python3
#coding=utf-8

# 匿名函数的定义

func = lambda x,y : x+y

result = func(1,2)
print(result)

# 匿名函数的应用1
# 为字典列表排序

infors =[{'age':19},{'age':28},{'age':17}]
print(infors)
infors.sort(key=lambda x:x['age'])

print(infors)

# 匿名函数的应用2

def test(a,b,func):
	result = func(a,b)
	print(result)

test(1,2,lambda x,y : x+y)


new_func = input("请输入一个匿名函数:")
new_func = eval(new_func)
test(3,4,new_func)
