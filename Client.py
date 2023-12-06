import socket

class Client:
    def __init__(self):
        self.host = ''
        self.port = 3000
        self.client_socket =''

    def setup(self, host, port):
        self.host = host
        self.port = port

    def connect(self):
        self.client_socket = socket.socket()
        self.client_socket.connect((self.host, self.port))

    def send_message(self, message):
        self.client_socket.send(message.encode())

    def start(self, host, port):
        self.setup(host, port)
        self.connect()
