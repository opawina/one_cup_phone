import json
import socket
from time import time


class JsonSocketConnector:

    def __init__(self, sock):

        self.sock__ = sock
        self.json_tmpl = {
            "action": None,
            "time": None,
            "message": None
        }

    def send(self, data):

        buf = json.dumps(data)
        buf = buf.encode()

        self.sock__.send(buf)

    def recv(self):

        recv_data = self.sock__.recv(1024)

        recv_data = recv_data.decode()
        recv_data = json.loads(recv_data)

        return recv_data


class Client(JsonSocketConnector):

    def __init__(self, host):

        self.sock = socket.socket(
            family=socket.AF_INET,
            type=socket.SOCK_STREAM,
            proto=0
        )
        self.sock.connect(host)
        super().__init__(self.sock)

        print('+CLIENT START+')

    def close(self):

        self.sock.close()
        print('+CLOSE CONNECTION+')


class Server(JsonSocketConnector):

    def __init__(self, host):

        self.sock = socket.socket(
            family=socket.AF_INET,
            type=socket.SOCK_STREAM,
            proto=0
        )
        self.sock.bind(host)
        self.sock.listen(5)

        super().__init__(self.sock)

        print('+SERVER START+\nListening...')

    def accept(self):

        return self.sock.accept()

    def close(self):

        self.sock.close()
        print("+STOP SERVER+")










