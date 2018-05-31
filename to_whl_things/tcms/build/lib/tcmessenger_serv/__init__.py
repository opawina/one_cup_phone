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

Если Новый Юзер то добавляет в БД. -> Новый пользователь в таблицу Юзеров.
Если Старый юзер то С ищет его в таблице Юзеры. Авторизует если ок,
иначе говорит К что такого нет.

С передает авторизованному К Список контактов и ждет заказ на чат.

Получает от К заказ на Приватный или Групповой чат. Создает его, приглашая
Собеседника\ов. Пересылает сбщ между собеседниками. Пишет в БД весь чат.

В случае отключения участника чата С уведомляет остальных.

С закрываает чат если отключился последний участник.

'''

import json
from select import select
import os
from socketserver import StreamRequestHandler, ThreadingTCPServer
import threading
from time import time, ctime
import queue
from time import sleep


from MessagerClasses.Server import Server
from MessagerClasses.DataBaseAPI import DataBaseAPI
from utils.cli_handler import cli_handler
from utils.logging_ import log
from utils.db_initiation import db_initiation
from utils import hasher



@log
class CTCPHandler(StreamRequestHandler):

    def handle(self):

        self.connection.settimeout(0.5)

        print("New connection:", self.client_address)
        host = self.client_address[0] + ':' + str(self.client_address[1])

        dbapi = DataBaseAPI()

        try:
            ###############################################
            # авторизация клиента
            authoriz = self.rfile.readline().decode()
            authoriz = json.loads(authoriz.replace('\n', ''))

            login = authoriz['login']
            passw = authoriz['passw']

            if authoriz['new_user']:
                try: # обрабатываю если юзер-логин уже существует
                    dbapi.add_new_user(login, host, passw)
                    print('NEW USER WAS ADD')
                except Exception as E:
                    # print(E)
                    print('LOGIN "{}" ALREADY EXIST'.format(login))

            else:
                print('OLD USER')
                authoriz_fact = dbapi.authorization_user(login, passw)
                if authoriz_fact:
                    print('USER WAS AUTHORIZED')
                else:
                    print('UKNOWN USER')



            ################################################
            # основная работа

            list_hosts.append(self.client_address)

            msg = 100

            while True:

                # try:
                #     msg = q.get(block=False)
                #     print('FROM Q:', msg)
                # except:
                #     pass
                #
                # if msg:

                try: # обрабатываю Е если клиент отвалился
                    print('SEND', msg)
                    self.wfile.write((str(msg) + ctime()).encode())
                    msg += 100
                except:
                    print(self.client_address, 'CLIENT WAS CLOSED CONNECTION')
                    list_hosts.remove(self.client_address)
                    break

                try:
                    data = self.rfile.readline().decode()[:-1]

                    if data == 'ss':
                        print(self.client_address, 'BREAK')
                        break

                    if data:
                        q.put(data)
                        print(self.client_address, '->', data)

                except Exception as E:
                    pass
                    # print('EXCEPTION:', E)

                print(list_hosts)
                sleep(8)


        except:
            raise
            print('Client closed connection')




if __name__ == '__main__':

    socket_, user_data = cli_handler()

    # Если не было, создаем на сервере БД с необходимыми таблицами.
    if not 'twocups.db' in os.listdir('dwh'):
        db_initiation()

    class CThreadingTCPServer(ThreadingTCPServer):pass

    list_hosts = []
    q = queue.Queue()
    msg = None
    server = CThreadingTCPServer(socket_, CTCPHandler)

    server_thread = threading.Thread(target=server.serve_forever())
    server_thread.daemon = False
    server_thread.start()

    server.shutdown()
    server.server_close()




'''

cd PycharmProjects\one_cup_phone
'''