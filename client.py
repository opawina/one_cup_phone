'''
Beautiful code!
'''

import socket
from multiprocessing import Process, current_process, Queue
import json

from MessagerClasses.Client import Client
from utils.cli_handler import cli_handler
from utils.logging_ import log
from MessagerClasses.JsonSocketConnector import msg_tmpl_client


from time import sleep

# @log
# def main():


def sock_work(recv_inpt, inpt_send):

    global received
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
            client.sendall(bytes(send, 'utf-8'))
            send = None

        try:
            received = str(client.recv(1024), "utf-8")
            print('\nRECEIVED:' + received)
            if received:
                recv_inpt.put(received)
        except Exception as E:
            pass
            # print('EXCEPTION:', E)



if __name__ == '__main__':

    socket_, user_data = cli_handler()

    with Client(socket_, user_data) as client:

        # основная работа
        print('оосновная работа')

        recv_inpt = Queue()
        inpt_send = Queue()

        p1 = Process(target=sock_work, args=(recv_inpt, inpt_send,))
        p1.start()

        recvinpt = None

        while True:

            try:
                recvinpt = recv_inpt.get(block=False)
            except:
                pass

            if recvinpt == 'END':
                recv_inpt.close()
                inpt_send.close()
                print('CLOSE MESSENGER')
                break

            print('GET:', recvinpt)
            if recvinpt:

                send = input('ENTER MSG ->') + '\n'
                print(send, send, send)

                if send.replace('\n', '') == 'ss':
                    break

                inpt_send.put(send)

                received = None
            sleep(3)




'''

cd PycharmProjects\one_cup_phone
'''