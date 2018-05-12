'''
МЕСЕНДЖЕР TwoCups (далее М).

Концепция:
(концепция является ориентиром и реализация может отличаться)

СЕРВЕР (далее С) делает все (см. далее).

КЛИЕНТ (далее К) очень легкий\тонкий, что бы работал даже на ламповом
калькуляторе.
Поэтому у К нет БД. Все запрашивается у сервера.
Так же это решает проблему с историей сбщ и контактами если зайти с другого
устройства или если устройство погибнет в луже или устройство украдут и будут
читать сбщ.
Напротив, С бэкапится и секурный.

Юзер заходит в М либо создавая нового Юзера либо представляется как уже
существующий в БД сервера.
(дописать суть авторзации (пароль? ключ? ...))

Если К авторизован то получает свой Список контактов от С.

К может в любой момент запросить Весь список Юзеров (онлайн или вообще весь?) и
начать чатиться с любым из них, либо выбрать Юзера из своего Списка
контактов. Собеседник автоматически добавляется в Список контактов при
начале чата, если его там доселе небыло.
К может удалить Юзера из Списка контактов.

К может создавать приватный или групповой чат.

К может выйти из чата.


Жизнь С:
С принимает авторизационное сбщ от К.

Если Новый Юзер то добавляет в БД. -> Новый пользователь в таблицу Юзеров. А
так же для каждого юзера создается таблица История_сбщ и таблица Лист_контактов.
Если Старый юзер то С ищет его в таблице Юзеры. Авторизует если ок,
иначе говорит К что такого нет.

С передает авторизованному К Список контактов и ждет сбщ.

Получает от К заказ на Приватный или Групповой чат. Создает его, приглашая
Собеседника\ов. Пересылает сбщ между собеседниками. Пишет в БД весь чат.

В случае отключения участника чата С уведомляет остальных.

С закрываает чат если отключился последний участник.

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



class DBase:

    '''
    На стороне клиента хранится только список контактов.

    '''






'''

cd PycharmProjects\one_cup_phone
'''


