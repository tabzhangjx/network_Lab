from socket import *
# 创建socket
tcpClientSocket = socket(AF_INET, SOCK_STREAM)
# 链接服务器
serAddr = ('192.168.31.203', 7788)
tcpClientSocket.connect(serAddr)




# 提示用户输入数据
ID = input("请输入用户名：")
aa1=ID.encode('utf8')

pas = input("请输入密码：")
aa2=pas.encode('utf8')

tcpClientSocket.send(aa1)
tcpClientSocket.send(aa2)
# 接收对方发送过来的数据，最大接收1024个字节

recvData = tcpClientSocket.recv(1024)
bbb=recvData.decode('utf-8')
print('接收到的数据为:', bbb)
# 关闭套接字
tcpClientSocket.close()