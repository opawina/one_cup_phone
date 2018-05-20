from MessagerClasses.CJsonSocketConnector import JsonSocketConnector
from utils.logging_ import log


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

