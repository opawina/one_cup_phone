import json
import socket
from time import time

from utils.logging import logging_


class JsonSocketConnector:

    @logging_
    def __init__(self):

        self.sock = socket.socket(
            family=socket.AF_INET,
            type=socket.SOCK_STREAM,
            proto=0
        )
        self.json_tmpl = {
            "action": None,
            "time": None,
            "message": None
        }

    def send_(self, data):

        buf = json.dumps(data)
        buf = buf.encode()

        self.sock.send(buf)

    def recv_(self):

        recv_data = self.sock.recv(1024)

        recv_data = recv_data.decode()
        recv_data = json.loads(recv_data)

        return recv_data


class Client(JsonSocketConnector):

    @logging_
    def __init__(self, host):

        super().__init__()

        # self.sock = socket.socket(
        #     family=socket.AF_INET,
        #     type=socket.SOCK_STREAM,
        #     proto=0
        # )
        self.sock.connect(host)

        print('+CLIENT START+')

    def close(self):

        self.sock.close()
        print('+CLOSE CONNECTION+')


class Server(JsonSocketConnector):

    def __init__(self, host):

        super().__init__()
        # self.sock = socket.socket(
        #     family=socket.AF_INET,
        #     type=socket.SOCK_STREAM,
        #     proto=0
        # )
        self.sock.bind(host)
        self.sock.listen(5)

        self.sub_sock = None
        self.sub_addr = None


        print('+SERVER START+\nListening...')

    def accept_(self):

        self.sub_sock, self.sub_addr = self.sock.accept()

        print('New connect : {}'.format(self.sub_addr))

        return self.sub_sock, self.sub_addr

    def close(self):

        self.sock.close()
        print("+STOP SERVER+")










