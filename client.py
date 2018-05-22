'''
Beautiful code!
'''

import socket
from multiprocessing import Process, current_process, Queue

from MessagerClasses.CClient import Client
from utils.cli_handler import cli_handler
from utils.logging_ import log


from time import sleep
# @log
# def main():


socket_ = cli_handler()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5)


def sock_work(recv_inpt, inpt_send):

    global received

    print('SOCK WORK BEGINS')
    print(current_process().name)

    try:
        sock.connect(socket_)

        global send
        send = None

        while True:
            # print('IN SOCK LOOP')

            try:
                send = inpt_send.get(block=False)
                print('SEND IN RECV LOOP:', send)
            except Exception as E:
                pass
                # print(E)

            if send:
                print('SEND')
                sock.sendall(bytes(send, 'utf-8'))
                send = None

            try:
                received = str(sock.recv(1024), "utf-8")
                print('\nRECEIVED:' + received)
                if received:
                    recv_inpt.put(received)
            except Exception as E:
                pass
                # print('EXCEPTION:', E)


    finally:
        print('END')
        sock.close()


if __name__ == '__main__':

    recv_inpt = Queue()
    inpt_send= Queue()

    p1 = Process(target=sock_work, args=(recv_inpt, inpt_send, ))
    p1.start()

    # received = 1
    print(current_process().name)
    while True:

        recvinpt = recv_inpt.get()
        print('GET:', recvinpt)

        if recvinpt:

            send = input('ENTER MSG ->') + '\n'
            print(send,send,send)

            if send.replace('\n', '') == 'ss':
                break

            inpt_send.put(send)

            # received = None
        # sleep(3)







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