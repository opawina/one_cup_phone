#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
Beautiful code!
'''

import json

from Classes import Server
from utils.cli_handler import cli_handler
from utils.logging import logging_

# не знаю как использовать методы суперкласса в классе Server

@logging_
def main():

    socket_ = cli_handler()
    sock = Server(socket_)

    ##########################################################################
    # не знаю как использовать методы суперкласса в классе Server
    sub_sock, sub_addr = sock.accept_()

    # print('New connect : {}'.format(sub_addr))

    recv_data = sub_sock.recv(1024)
    recv_data = recv_data.decode()
    recv_data = json.loads(recv_data)

    print('Received data: {0}'.format(recv_data['message']))

    dic_tmpl = {
        2: 3,
        3: "Welcome!"
    }
    dic_tmpl = json.dumps(dic_tmpl)
    dic_tmpl = dic_tmpl.encode()

    sub_sock.send(dic_tmpl)
    print('Send welcom to client')

    while True:
        recv_data = sub_sock.recv(1024)
        recv_data = recv_data.decode()
        recv_data = json.loads(recv_data)

        print('Received data: {0}'.format(recv_data['message']))

        ###########################################################################

        # conn, con_addr = sock.accept()
        # print('New connect : {}'.format(con_addr))


        # answer = useful_work(conn)
        #
        if recv_data['message'] == 'stop server':
            break

    sock.close()


def useful_work(conn):
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