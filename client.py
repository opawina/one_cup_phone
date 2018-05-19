'''
Beautiful code!
'''

import socket
from multiprocessing import Process

from MessagerClasses.CClient import Client
from utils.cli_handler import cli_handler
from utils.logging import log



# @log
def main():

    socket_ = cli_handler()

    # global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    try:

        sock.connect(socket_)

        received = None

        def inpt(sock):

            # nonlocal sock

            while True:

                if received:
                    print(received)

                data = input() + '\n'

                if data == 'ss':
                    break

                sock.sendall(bytes(data, 'utf-8'))

        def recv(sock):

            # nonlocal sock

            nonlocal received

            print('RECV')
            while True:
                received = str(sock.recv(1024), "utf-8")
                print(received)

        print(2)
        p2 = Process(target=recv, args=(sock,))
        print(2)
        p1 = Process(target=inpt, args=(sock,))
        print(2)

        print(1)
        p2.start()
        print(1)
        p1.start()

    finally:
        print('END')
        sock.close()







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






if __name__ == '__main__':
    main()



'''

cd PycharmProjects\one_cup_phone
'''