import socket
from product import Product
import pickle

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("0.0.0.0", 4571))

    python_dictionary = {"a": 1, "b": 2}
    picked_dictionary = pickle.dumps(python_dictionary)

    custom_object = Product("P024", "Torch", 13)
    picked_object = pickle.dumps(custom_object)

    s.listen(5)

    print("Server is up. Listening for connections...")

    client, address = s.accept()
    print("Connection to", address, "established\n")
    print("Client object", client, "\n")

    client.send(python_dictionary)
    client.send(custom_object)