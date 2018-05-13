#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
Beautiful code!
'''

import json
from select import select
import os

from Classes import Server
from utils.cli_handler import cli_handler
from utils.logging import log
from utils.db_initiation import db_initiation


@log
def main():

    socket_ = cli_handler()
    with Server(socket_) as sockk:

        # Если не было, создаем на сервере БД с необходимыми таблицами.
        if not 'twocups.db' in os.listdir():
            db_initiation()

        b = 0
        while True:

            break_ = False
            r, w, e = [], [], []
            socks = sockk.accept_()
            try:
                r, w, e = select(socks, socks, socks, 0)
            except Exception as e:
                pass

            for sock_r in r:
                try:
                    recv_data = sock_r.recv(1024)
                    recv_data = recv_data.decode()
                    recv_data = json.loads(recv_data)
                    print(recv_data['message'])
                except:
                    print('r CLIENT SOCKET CLOSED', sock_r)
                    socks.remove(sock_r)
                else:
                    if recv_data['message'] == 'ss':
                        break_ = True
                finally:
                    recv_data = json.dumps(recv_data)
                    recv_data = recv_data.encode()

                    for sock_w in w:
                        try:
                            sock_w.send(recv_data)
                        except:
                            print('w CLIENT SOCKET CLOSED', sock_w)
                            socks.remove(sock_w)


            if break_:
                break
        # явно не закрываем соединеие т.к. используется менеджер контекста





if __name__ == '__main__':
    main()





'''

cd PycharmProjects\one_cup_phone
'''