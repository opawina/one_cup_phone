from MessagerClasses.CJsonSocketConnector import JsonSocketConnector
from utils.logging_ import log


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
