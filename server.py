import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("localhost", 4571))
s.listen(5)