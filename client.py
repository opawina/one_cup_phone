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

    print('+CLIENT START+')
    sock = socket.socket(family=socket.AF_INET,
                         type=socket.SOCK_STREAM,
                         proto=0)
    sock.connect(socket_)
    print('CONNECTED TO : {0}'.format(socket_))
    useful_work(sock)
    print(3)
    sock.close()
    print('CLOSED')


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


def useful_work(conn):
    payload = {
        "a1": "A!A!",
        "b2": "B@"
    }
    print('SENT {0}'.format(payload))
    payload = json.dumps(payload)
    payload = payload.encode('utf-8')
    conn.send(payload)

    while True:
        received_data = conn.recv(1024)
        if received_data:
            received_data = received_data.decode()
            received_data = json.loads(received_data)
            print('ANSWER FROM SERVER : {0}'.format(received_data['a1']))
            break



if __name__ == '__main__':
    main()
