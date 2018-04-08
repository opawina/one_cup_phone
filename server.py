#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
Beautiful code!
'''

import socket
import argparse
import json

from Classes import Server


def main():

    socket_ = cli_handler()
    sock = Server(socket_)

    while True:
        conn, con_addr = sock.accept()
        print('New connect : {}'.format(con_addr))
        answer = useful_work(sock, conn)

        if answer:
            break

    sock.close()
    print("STOP")


def cli_handler():
    parser = argparse.ArgumentParser(description='Default host is 127.0.0.1:7777')

    parser.add_argument('-a', '--addr', help='ip addres', default='127.0.0.1')
    parser.add_argument('-p', '--port', help='tcp port', type=int, default=7777)

    args = parser.parse_args()

    # ip string validating
    try:
        socket.inet_aton(args.addr)
    except:
        print('ip address is not correct')
        quit(3)

    return (args.addr, args.port)


def useful_work(sock, conn):
    # здороваемся
    received_data = conn.recv(1024)
    received_data = received_data.decode()
    received_data = json.loads(received_data)
    print('Received data: {0}'.format(received_data['message']))

    dic_tmpl = {
        2: 3,
        3: "Welcome!"
    }
    dic_tmpl = json.dumps(dic_tmpl)
    dic_tmpl = dic_tmpl.encode()

    conn.send(dic_tmpl)
    print('Send welcom to client')

    # обслуживаем
    while True:
        received_data = conn.recv(1024)
        if received_data:
            received_data = received_data.decode()
            received_data = json.loads(received_data)

            if received_data["message"] == "stop server":
                return 1

            print('Received data: {0}'.format(received_data['message']))



if __name__ == '__main__':
    main()







'''

cd PycharmProjects\one_cup_phone
'''