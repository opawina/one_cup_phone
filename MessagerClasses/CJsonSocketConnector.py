import json
import socket

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



'''

cd PycharmProjects\one_cup_phone
'''


