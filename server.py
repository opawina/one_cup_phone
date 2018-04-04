#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
Beautiful code!
'''

import socket
import sys
import getopt
import json


def main():
    socket_ = cli_handler()

    sock = socket.socket(family=socket.AF_INET,
                         type=socket.SOCK_STREAM,
                         proto=0)
    sock.bind(socket_)
    sock.listen(5)

    print('+SERVER START+\nListening...')

    while True:
        conn, con_addr = sock.accept()
        print('New connect : {}'.format(con_addr))
        answer = useful_work(sock, conn)

        if answer:
            break

    sock.close()
    print("STOP")


def cli_handler():
        try:
            opts, args = getopt.getopt(sys.argv[1:],
                                       "ha:p:",
                                       ["help", "address=", "port="])
        except getopt.GetoptError as err:
            print(err)
            sys.exit(2)

        # default connection settings
        address = 'localhost'
        port = 7777

        for opt, arg in opts:
            if opt in ("-h", "--help"):
                print('''    server.py [-a, --address] <address> [-p, --port] <port>
        default connection settings {0}:{1}'''.format(address, port))
            elif opt in ("-a", "--address"):
                address = arg
            elif opt in ("-p", "--port"):
                port = arg

        return (address, port)


def useful_work(sock, conn):
    # здороваемся
    received_data = conn.recv(1024)
    received_data = received_data.decode()
    received_data = json.loads(received_data)
    print('Received data: {0}'.format(received_data))

    dic_tmpl = {
        "article": "connect",
        "message": "key2"
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