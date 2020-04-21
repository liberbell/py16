import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.bind(("0.0.0.0", 4571))
    s.settimeout(5)

    try:
        s.listen(5)

        print("Server is up. Listening for connections...")

        client, address = s.accept()
        print("Connection to ...", address, "established\n")
        print("Client Object:", client, "\n")

        client.send(bytes("Hello! Welcome to socket programming.", "utf-8"))

    except:
        print("Timeout has been execeeded. Close the connection...")