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
    sockk = Client(socket_)

    # аутентификация
    json_tmpl = sockk.json_tmpl
    json_tmpl['message'] = "Can I come in?"
    sockk.send_(json_tmpl)
    recieve_data = sockk.recv_()
    print(recieve_data['3'], 'from server')

    # общаемся
    while True:
        inpt = input()
        sockk.json_tmpl['message'] = inpt
        sockk.send_(sockk.json_tmpl)

        if inpt == 'ss':
            break

    sockk.close()




if __name__ == '__main__':
    main()
