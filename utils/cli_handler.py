import socket
import argparse

from utils.logging_ import log
from config import HOST


ip = HOST.IP
port = HOST.PORT


@log
def cli_handler():

    parser = argparse.ArgumentParser(description='Default host is {}:{}'.format(ip, port))

    parser.add_argument('-a', '--addr', help='ip addres', default=ip)
    parser.add_argument('-p', '--port', help='tcp port', type=int, default=port)

    args = parser.parse_args()

    # validating ip string
    try:
        socket.inet_aton(args.addr)
    except:
        print('ip address is not correct')
        quit(3)

    return (args.addr, args.port)