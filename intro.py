import socket

print(socket.gethostname())
# print(socket.gethostbyname(socket.gethostname()))
print(socket.gethostbyaddr("127.0.0.1"))