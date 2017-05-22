#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com


from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
#新建一个用户组
authorizer = DummyAuthorizer()
#将用户名，密码，指定目录，权限 添加到里面
authorizer.add_user("guest", "guest", "/Users/ZRC/Documents/FTP", perm="elr")#adfmw
#这个是添加匿名用户,任何人都可以访问，如果去掉的话，需要输入用户名和密码，可以自己尝试
#authorizer.add_anonymous("D:/")

handler = FTPHandler
handler.authorizer = authorizer
#开启服务器
server = FTPServer(("49.140.11.252", 8000), handler)
server.serve_forever()