# -*- coding:UTF-8 -*-
import socket
import os

#设置监听主机

host = "192.168.1.193"  

#创建原始套接字，绑定在公开端口

if os.name == "nt":
    socket_protocol = socket.IPPROTO_IP
else :
    socket_protocol = socket.IPPROTO_ICMP

sniffer = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket_protocol)

sniffer.bind((host,0))

#设置在捕获的数据包中包含IP头

sniffer.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)


#Windows中设置IOCTL，启用混杂模式

if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)

#读取单个数据包

print sniffer.recvfrom(65565)

#关闭Windows平台的混杂模式

if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL,socket.RCVALL_OFF)
    
