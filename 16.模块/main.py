# import sendmsg
# sendmsg.test1()
# sendmsg.test2()

# from sendmsg import test1,test2
from sendmsg import * # 这里方法会被后面重名的方法覆盖
from recmsg import *

# sendmsg.test1() # 这个会报错,不能用sendmsg
test1()
test2()
test3()
