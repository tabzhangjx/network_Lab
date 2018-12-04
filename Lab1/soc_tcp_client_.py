from socket import *
# 创建socket
tcpClientSocket = socket(AF_INET, SOCK_STREAM)
# 链接服务器
serAddr = ('192.168.31.203', 7788)
tcpClientSocket.connect(serAddr)
# 提示用户输入数据
sendData = input("请输入要发送的数据：")
print(type(sendData))
aaa=sendData.encode('utf8')

tcpClientSocket.send(aaa)
# 接收对方发送过来的数据，最大接收1024个字节
recvData = tcpClientSocket.recv(1024)
bbb=recvData.decode('utf-8')
print('接收到的数据为:', bbb)
# 关闭套接字
tcpClientSocket.close()