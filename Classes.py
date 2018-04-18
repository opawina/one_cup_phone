import json
import socket
from time import time

from utils.logging import logging_


class JsonSocketConnector:

    @logging_
    def __init__(self):

        self.sock_main = socket.socket(
            family=socket.AF_INET,
            type=socket.SOCK_STREAM,
            proto=0
        )
        self.sock = None
        self.json_tmpl = {
            "action": None,
            "time": None,
            "message": None
        }

    @logging_
    def send_(self, data):

        buf = json.dumps(data)
        buf = buf.encode()
        print('sock in send', self.sock)
        self.sock.send(buf)

    @logging_
    def recv_(self):

        recv_data = self.sock.recv(1024)

        recv_data = recv_data.decode()
        recv_data = json.loads(recv_data)

        return recv_data



class Client(JsonSocketConnector):

    @logging_
    def __init__(self, host):

        super().__init__()

        self.sock = self.sock_main.connect(host)
        print('sock_main in client', self.sock_main)
        print('sock in client', self.sock)

        print('+CLIENT START+')

    @logging_
    def close(self):

        self.sock_main.close()
        self.sock.close()
        print('+CLOSE CONNECTION+')



class Server(JsonSocketConnector):

    @logging_
    def __init__(self, host):

        super().__init__()

        self.sock_main.bind(host)
        self.sock_main.listen(5)

        # self.sub_sock = None
        self.sub_addr = None

        print('+SERVER START+\nListening...')

    @logging_
    def accept_(self):

        self.sock, self.sub_addr = self.sock_main.accept()

        print('New connect : {}'.format(self.sub_addr))

        # return self.sock, self.sub_addr

    @logging_
    def close(self):

        self.sock_main.close()
        self.sock.close()
        print("+STOP SERVER+")










