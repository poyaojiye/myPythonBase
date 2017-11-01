

# 写入文件
f = open("test.txt","w")
f.write("hello world!\n")
f.write("hello world!\n")
f.write("hello world!\n")
f.write("hello world!\n")
f.close()

# 读取文件
f = open("test.txt","r")
content = f.read()
print(content)
f.close()

# 复制文件

file_name = input("请输入需要复制的文件名：")
# 获取新的文件名

new_file_name = file_name[0:file_name.rfind(".")] + "[复件]" + file_name[file_name.rfind("."):]
print(new_file_name)

# 打开源文件
source_file = open(file_name,"r")

# 打开新文件
des_file = open(new_file_name,"w")

content = source_file.read()
des_file.write(content)

source_file.close()
des_file.close()
