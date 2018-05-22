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
sock.setblocking(1)

def sock_work(q):
    sock_work.qq = None
    global received

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

            try:
                received = str(sock.recv(1024), "utf-8")
                print('\n' + received)
                q.put(received)
            except Exception as E:
                pass
                # print('EXCEPTION:', E)


    finally:
        print('END')
        sock.close()


if __name__ == '__main__':

    q = Queue()

    p1 = Process(target=sock_work, args=(q, ))
    p1.start()

    received = 1
    print(current_process().name)
    while True:

        ii = q.get()
        print('GET:', ii)

        if ii:

            msg = input('ENTER MSG ->') + '\n'

            if msg.replace('\n', '') == 'ss':
                break

            received = None
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