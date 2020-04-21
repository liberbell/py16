import socket
from product import Product

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind("0.0.0.0", 4571)
    python_dictionary = {"a": 1, "b": 2}