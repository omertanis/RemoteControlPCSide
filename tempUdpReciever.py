import socket

UDP_IP = "192.168.2.69"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(64)
    print "received message:", data





# # --------TCP-----------
# # !/usr/bin/env python
# import socket
#
#
# TCP_IP = '127.0.0.1'
# TCP_PORT = 5005
# BUFFER_SIZE = 1024
# MESSAGE = "H"
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((TCP_IP, TCP_PORT))
# while True:
#     s.send(MESSAGE)
# s.close()
