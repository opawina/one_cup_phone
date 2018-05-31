import socket

from MessagerClasses.JsonSocketConnector import JsonSocketConnector

from utils.logging_ import log


class Client():

    '''
    При создании экземпляра класса:
        Создается подключеине.
        Коннект и обработка исключений
        Авторизация.
        ...

    '''

    @log
    def __init__(self, sock_, user_data):

        print('STARTING MESSENGER...')

        self.user_data = user_data

        self.tmpl_msg = JsonSocketConnector()

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(5)

        try: # обрабатываю если сервер не товечает
            self.sock.connect(sock_)
            print('CONNECTED TO SERVER')

            self.authorization()

        except ConnectionRefusedError:
            print('SERVER DID NOT RESPOND')
            # self.__exit__()

        except Exception as E:
            raise

    @log
    def authorization(self):

        bmsg = self.tmpl_msg.tmpl_authorization(self.user_data)
        self.sock.sendall(bmsg)



    def __enter__(self):
        return self

    @log
    def __exit__(self, exc_type, exc_val, exc_tb):

        self.sock.close()
        print('MESSENGER CLOSED')

