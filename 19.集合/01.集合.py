
# 集合中不能重复
a = {11,11,22,33,44,22}
print(a)

# 列表去重的方法

b = [11,11,22,33,44,22]
print(b)

# 转为集合去重
test = set(b)
print(test)
b = list(test)
# 转为列表排序
b.sort()
print(b)
