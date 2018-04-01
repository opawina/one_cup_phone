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
    sock.bind(socket_)
    sock.listen(5)
    print(1)
    while True:
        conn, con_addr = sock.accept()
        print('    New connect : {}'.format(con_addr))
        useful_work(conn)
        conn.close()


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
    print(2)
    received_data = conn.recv(1024)
    received_data = json.dumps(received_data.decode())
    print('    Received data:'.format(received_data))




if __name__ == '__main__':
    main()
