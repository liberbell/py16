import socket
from product import Product
import pickle

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("localhost", 4571))

    while True:
        msg = s.recv(1024)
        if not msg:
            print("No message from the server.Closing the connection...")
            break

        # print("Message from server:", msg.decode("utf-8"))
        print("Type of recieved message", type(msg))
        print("Message data:", msg)

        unpicked_data = pickle.loads(msg)

        print("Type of deserialized message:", type(unpicked_data))
        print("Deserialized data:", unpicked_data)