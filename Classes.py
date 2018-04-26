'''
Месенджер. Все со всеми (Групповой чат). Пока.
Сервер принимает от клиента и передает всем подключениям.
'''


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
        self.socks_write = []
        self.socks_read = []
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
        self.sock.settimeout(1)

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
        self.sock_main.settimeout(1)

        self.client_socks = []

        print('+SERVER START+\nListening...')


    def __enter__(self):

        return self


    @log
    def __exit__(self, exc_type, exc_val, exc_tb):

        self.sock_main.close()
        if self.client_socks:
            [sock.close() for sock in self.client_socks]

        print("+STOP SERVER+")


    @log
    def accept_(self):

        try:
            sock, sub_addr = self.sock_main.accept()
            self.client_socks.append(sock)
            print('New connect: {}'.format(sub_addr))
        except OSError as e:
            pass

        return self.client_socks







'''

cd PycharmProjects\one_cup_phone
'''


