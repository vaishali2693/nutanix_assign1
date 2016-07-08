import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

sock.sendto("connection", ('127.0.0.1', 4242))

while True:
    msg, b = sock.recvfrom(1024)
    print msg
    sock.sendto("hello world",('127.0.0.1', 4242))

