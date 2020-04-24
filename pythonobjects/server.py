import socket
from product import Product
import pickle
import time

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("0.0.0.0", 4571))

    # python_dictionary = {"a": 1, "b": 2}
    # pickled_dictionary = pickle.dumps(python_dictionary)

    # custom_object = Product("P024", "Torch", 13)
    # pickled_object = pickle.dumps(custom_object)

    custom_products = [Product("P024", "Torch", 13),
                       Product("P025", "WaterBottle", 5),
                       Product("P026", "Keyboard", 20),
                       Product("P027", "Mouse", 15),
                       Product("P028", "USBCable", 2)]

    # print("Serialized dictionary type:", type(pickled_dictionary))
    # print("Serialized object type:", type(pickled_object))

    s.listen(5)

    print("Server is up. Listening for connections...")

    client, address = s.accept()
    print("Connection to", address, "established\n")
    print("Client object", client, "\n")

    # client.send(pickled_dictionary)
    client.send(pickled_object)