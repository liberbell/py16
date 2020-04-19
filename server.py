import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("", 4571))
s.listen(5)

print("Server is up. Listening for connections...")

client, address = s.accept()
print("Connection to ...", address, "established\n")
print("Client Object:", client, "\n")
