#!/usr/bin/env python
import socket
import socket_util as su

TCP_IP = '127.0.0.1'
TCP_PORT = 5555
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
data = s.recv(BUFFER_SIZE)
print data
su.sendAll(s,MESSAGE)
s.close()



print "received data:", data
