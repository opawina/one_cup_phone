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
    sock = start_client(socket_)
    useful_work(sock)
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


def start_client(socket_):
    print('+CLIENT START+')
    sock = socket.socket(family=socket.AF_INET,
                         type=socket.SOCK_STREAM,
                         proto=0)
    sock.connect(socket_)
    print('CONNECTED TO : {0}'.format(socket_))

    return sock


def useful_work(conn):
    dic_tmpl = {
        "article": "connect",
        "message": "key1"
    }

    # здороваемся
    print('SENT {0}'.format(dic_tmpl))
    dic_tmpl = json.dumps(dic_tmpl)
    dic_tmpl = dic_tmpl.encode('utf-8')
    conn.send(dic_tmpl)

    received_data = conn.recv(1024)
    if received_data:
        print(101)
        received_data = received_data.decode()
        received_data = json.loads(received_data)
        print('ANSWER FROM SERVER : {0}'.format(received_data['message']))

    # cli
    while True:
        msg = input()

        dic_tmpl = {}
        dic_tmpl["article"] = "canal"
        dic_tmpl["message"] = msg
        dic_tmpl = json.dumps(dic_tmpl)
        dic_tmpl = dic_tmpl.encode('utf-8')
        conn.send(dic_tmpl)

        if msg == "stop server":
            return 1


if __name__ == '__main__':
    main()
