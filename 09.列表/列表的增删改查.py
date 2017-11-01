
print("python里的列表类似数组，不同之处在于可以存放不同数据类型的数据")


print("=========增===============")
xiyouji = ['唐僧','孙悟空']
print(xiyouji)
xiyouji.append('猪八戒')
print(xiyouji)
xiyouji.insert(2,'沙僧')
print(xiyouji)
shenxian = ['观音菩萨','太上老君']
xiyouji.extend(shenxian)
print(xiyouji)

print("=========删===============")
xiyouji.pop()
print(xiyouji)
xiyouji.remove('观音菩萨')
print(xiyouji)
del xiyouji[0]
print(xiyouji)
print("列表也可以用下表的方式处理，类似字符串的下表")

print("=========改===============")
xiyouji[2] = '天蓬元帅'
print(xiyouji)

print("=========查===============")
print("天蓬元帅" not in xiyouji)
print("孙悟空" in xiyouji)
print(xiyouji)
