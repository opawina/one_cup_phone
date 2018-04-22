import json
import socket
from time import time

from utils.logging import log


class JsonSocketConnector:

    @log
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

    @log
    def send_(self):

        buf = json.dumps(self.json_tmpl)
        buf = buf.encode()

        self.sock.send(buf)

    @log
    def recv_(self):

        recv_data = self.sock.recv(1024)

        recv_data = recv_data.decode()
        recv_data = json.loads(recv_data)

        return recv_data



class Client(JsonSocketConnector):

    @log
    def __init__(self, host):

        super().__init__()

        self.sock = self.sock_main
        self.sock.connect(host)

        print('+CLIENT START+')

    def __enter__(self):
        return self

    @log
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock_main.close()
        self.sock.close()

        print('+CLOSE CONNECTION+')



class Server(JsonSocketConnector):

    @log
    def __init__(self, host):

        super().__init__()

        self.sock_main.bind(host)
        self.sock_main.listen(5)

        print('+SERVER START+\nListening...')

    def __enter__(self):
        return self

    @log
    def __exit__(self, exc_type, exc_val, exc_tb):

        self.sock_main.close()
        self.sock.close()

        print("+STOP SERVER+")

    @log
    def accept_(self):

        self.sock, self.sub_addr = self.sock_main.accept()

        print('New connect: {}'.format(self.sub_addr))





'''

cd PycharmProjects\one_cup_phone
'''


