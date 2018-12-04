from socket import *
# 创建socket
tcpSerSocket = socket(AF_INET, SOCK_STREAM)
# 绑定本地信息
address = ('', 7788)
tcpSerSocket.bind(address)
# 使用socket创建的套接字默认的属性是主动的，使用listen将其变为被动的，这样就可以接收别人的链接了
tcpSerSocket.listen(50)
# 如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务器
# newSocket用来为这个客户端服务
# tcpSerSocket就可以省下来专门等待其他新客户端的链接
newSocket, clientAddr = tcpSerSocket.accept()



a=['zjx','wyh']
print(a[1])
# 接收对方发送过来的数据，最大接收1024个字节
ID = newSocket.recv(1024)
aa1 = ID.decode('utf8')
pas = newSocket.recv(1024)
aa2 = pas.decode('utf8')

# 发送一些数据到客户端


if (aa1==a[1] and aa2==a[0]) or (aa1==a[0] and aa2==a[1]):
	sendata="success!"
else:
	sendata="failure!"

bbb=sendata.encode('utf-8')
newSocket.send(bbb)
# 关闭为这个客户端服务的套接字，只要关闭了，就意味着为不能再为这个客户端服务了，如果还需要服务，只能再次重新连接
newSocket.close()