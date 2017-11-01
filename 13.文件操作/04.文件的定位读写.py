

f = open("test.txt","r")
f.tell()
content = f.readline()
print(content)
f.tell()
f.seek(0,0)
content = f.readline()
print(content)
