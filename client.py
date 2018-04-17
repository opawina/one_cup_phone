#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
Beautiful code!
'''

from time import time

from Classes import Client
from utils.cli_handler import cli_handler
from utils.logging import logging_


@logging_
def main():

    socket_ = cli_handler()
    sock = Client(socket_)

    # аутентификация
    json_tmpl = sock.json_tmpl
    json_tmpl['message'] = "Can I come in?"
    sock.send_(json_tmpl)
    recieve_data = sock.recv_()
    print(recieve_data['3'], 'from server')

    # общаемся
    while True:
        inpt = input()
        sock.json_tmpl['message'] = inpt
        sock.json_tmpl['time'] = time()
        sock.send_(sock.json_tmpl)

        if inpt == 'ss':
            break

    sock.close()






if __name__ == '__main__':
    main()
