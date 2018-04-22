#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
Beautiful code!
'''

import json
from select import select

from Classes import Server
from utils.cli_handler import cli_handler
from utils.logging import log


@log
def main():

    socket_ = cli_handler()
    with Server(socket_) as sockk:

        b = 0
        while True:
            b += 3000
            r, w, e = [], [], []
            socks = sockk.accept_()

            try:
                r, w, e = select(socks, socks, socks, 0)
            except Exception as e:
                print(1111111, e)

            for sock in w:
                a = b
                a = json.dumps(a)
                sock.send(a.encode())


            # recive = sockk.recv_()
            # print('From client:', recive['message'])
            #
            # sockk.json_tmpl['message'] = 'Welcome!'
            # sockk.send_()
            #
            # while True:
            #     recive = sockk.recv_()
            #     print(recive['message'])
            #
            #     if recive['message'] == 'ss':
            #         break





if __name__ == '__main__':
    main()







'''

cd PycharmProjects\one_cup_phone
'''