

f = open("test.txt","w")
f.write("1.hello world!\n")
f.write("2.hello world!\n")
f.write("3.hello world!\n")
f.write("4.hello world!\n")
f.close()

f = open("test.txt","r")
content = f.read()
print(content)
f.close()
