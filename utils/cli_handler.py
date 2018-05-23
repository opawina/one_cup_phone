import socket
import argparse

from utils.logging_ import log
from config import HOST


ip = HOST.IP
port = HOST.PORT


@log
def cli_handler():

    parser = argparse.ArgumentParser(description='Default host is {}:{}'.format(ip, port))

    parser.add_argument('--addr', help='ip addres', default=ip)
    parser.add_argument('--port', help='tcp port', type=int, default=port)
    parser.add_argument('-n', '--new_usr', help='if u are new user', default=False, action='store_true')
    parser.add_argument('-l', '--login', help='your login', type=str)
    parser.add_argument('-p', '--password', help='your pass', type=str)

    args = parser.parse_args()

    try: # validating ip string
        socket.inet_aton(args.addr)
    except:
        print('ip address is not correct')
        quit(3)

    return (args)


if __name__ == '__main__':
    cli_handler()