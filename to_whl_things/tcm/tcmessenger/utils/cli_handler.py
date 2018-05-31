import socket
import argparse

from utils.logging_ import log
from config import HOST


ip = HOST.IP
port = HOST.PORT

description = 'Default host is {}:{}'.format(ip, port)

@log
def cli_handler():

    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('--addr', help='ip addres', default=ip)
    parser.add_argument('--port', help='tcp port', type=int, default=port)

    parser.add_argument('-n', '--new_usr', help='if u are new user', default=False, action='store_true')
    # parser.add_argument('-l', '--login', help='your login', type=str, required=True)
    # parser.add_argument('-p', '--passw', help='your password', type=str, required=True)
    # для отадки
    parser.add_argument('-l', '--login', help='your login', type=str, default='dobi')
    parser.add_argument('-p', '--passw', help='your password', type=str, default='pass21')

    args = parser.parse_args()

    try: # validating ip string
        socket.inet_aton(args.addr)
    except:
        print('ip address is not correct')
        quit(3)

    socket_ = (args.addr, args.port)
    user_data = {
        'login': args.login,
        'passw': args.passw,
        'new_user': args.new_usr
    }

    return socket_, user_data


if __name__ == '__main__':
    # cli_handler()

    import setuptools
    print(setuptools.findall('..'))