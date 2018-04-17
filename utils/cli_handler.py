import socket
import argparse
from utils.logging import logging_


@logging_
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