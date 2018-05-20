'''
Beautiful code!
'''

import socket
from multiprocessing import Process, current_process

from MessagerClasses.CClient import Client
from utils.cli_handler import cli_handler
from utils.logging_ import log


from time import sleep
# @log
# def main():


socket_ = cli_handler()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# global send
send = None

def inpt():
    print('INPT BEGINS')
    print(current_process().name)

    # global send

    while True:
        print('IN INPT LOOP')

        # try:
        #     send = input('ENTER MSG ->') + '\n'
        #
        #     if send == 'ss':
        #         break
        # except EOFError as E:
        #     print(E)
        sleep(4)


def sock_work():
    print('SOCK WORK BEGINS')
    print(current_process().name)

    try:
        sock.connect(socket_)

        send = None

        while True:
            print('IN SOCK LOOP')

            if send:
                print('SEND')
                sock.sendall(bytes(send, 'utf-8'))
            send = None

            received = str(sock.recv(1024), "utf-8")
            print(received)

    finally:
        print('END')
        sock.close()


if __name__ == '__main__':

    p1 = Process(target=inpt)
    p2 = Process(target=sock_work)

    p1.start()
    p2.start()

    while True:
        print(current_process().name)
        sleep(1)







    # with Client(socket_) as sockk:
    #
    #     # общаемся
    #     while True:
    #         try:
    #             recv_data = sockk.recv_()
    #             print('RECIVE:', recv_data['message'])
    #         except:
    #             pass
    #         finally:
    #             inpt = input()
    #             sockk.json_tmpl['message'] = inpt
    #             sockk.send_()
    #
    #             if inpt == 'ss':
    #                 break
    # # явно не закрываем соединеие т.к. используется менеджер контекста






# if __name__ == '__main__':
    # main()



'''

cd PycharmProjects\one_cup_phone
'''