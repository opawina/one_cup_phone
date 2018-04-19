#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
Beautiful code!
'''

from time import time

from Classes import Client
from utils.cli_handler import cli_handler
from utils.logging import log


@log
def main():

    socket_ = cli_handler()
    sockk = Client(socket_)

    # аутентификация
    sockk.json_tmpl['message'] = "Can I come in?"
    sockk.send_()
    recieve_data = sockk.recv_()
    print('From server:', recieve_data['message'])

    # общаемся
    while True:
        inpt = input()
        sockk.json_tmpl['message'] = inpt
        sockk.send_()

        if inpt == 'ss':
            break

    sockk.close()




if __name__ == '__main__':
    main()
