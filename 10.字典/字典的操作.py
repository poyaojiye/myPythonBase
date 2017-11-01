
# 增加
map = {"name":"smart","sex":"male","age":27}
print(map)
map["add"] = "北京"
print(map)

# 删除
del map['add']

# 修改
map['age'] = 28

# 查询

print(map['name'])
print(map.get('name'))
