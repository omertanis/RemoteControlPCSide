#  UDP
import socket

UDP_IP = "192.168.2.69"
UDP_PORT = 5005
MESSAGE = "a"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

while True:
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))



# ------TCP-----
#!/usr/bin/env python

import socket


# TCP_IP = '127.0.0.1'
# TCP_PORT = 5005
# BUFFER_SIZE = 20  # Normally 1024, but we want fast response
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((TCP_IP, TCP_PORT))
# s.listen(1)
#
# conn, addr = s.accept()
# print 'Connection address:', addr
# while 1:
#     data = conn.recv(BUFFER_SIZE)
#     print "received data:", data
#
# conn.close()