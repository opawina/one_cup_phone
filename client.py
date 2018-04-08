#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
Beautiful code!
'''

import socket
import argparse
from time import time

from Classes import Client


def main():

    socket_ = cli_handler()
    sock = Client(socket_)

    # аутентификация
    json_tmpl = sock.json_tmpl
    json_tmpl['message'] = "Can I come in?"
    sock.send(json_tmpl)
    recieve_data = sock.recv()
    print(recieve_data['3'], 'from server')

    # общаемся
    while True:
        inpt = input()
        sock.json_tmpl['message'] = inpt
        sock.json_tmpl['time'] = time()
        sock.send(sock.json_tmpl)

        if inpt == 'stop server':
            break

    sock.close()


def cli_handler():

    parser = argparse.ArgumentParser(description='Default host is 127.0.0.1:7777')

    parser.add_argument('-a', '--addr', help='ip addres', default='127.0.0.1')
    parser.add_argument('-p', '--port', help='tcp port', type=int, default=7777)

    args = parser.parse_args()

    # validating ip string
    try:
        socket.inet_aton(args.addr)
    except:
        print('ip address is not correct')
        quit(3)

    return (args.addr, args.port)






if __name__ == '__main__':
    main()
