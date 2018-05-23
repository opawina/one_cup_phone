'''
Beautiful code!
'''

import socket
from multiprocessing import Process, current_process, Queue
import json

from MessagerClasses.CClient import Client
from utils.cli_handler import cli_handler
from utils.logging_ import log
from MessagerClasses.CJsonSocketConnector import msg_tmpl_client


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



if __name__ == '__main__':

    args_from_stdin = cli_handler()
    print(args_from_stdin)

    socket_ = (args_from_stdin.addr, args_from_stdin.port)

    # __init__ CClient
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)

    print('STARTING MESSENGER...')

    try: # обрабатываю Е если сервер не ответил
        sock.connect(socket_)

        # авторизация
        msg = msg_tmpl_client['authorization']
        msg['new_user'] = args_from_stdin.new_usr
        msg['login'] = args_from_stdin.login
        msg['passw'] = args_from_stdin.passw
        # print(json.dumps(msg) + '\n')
        # sock.sendall((json.dumps(msg) + '\n').encode())

        msg = json.dumps(msg) + '\n'
        print('*'+msg+'*')
        # msg = 'qwe1' + '\n'
        # sock.sendall(bytes(msg, 'utf-8'))
        sock.sendall(msg.encode())
        print(12)



        # recv_inpt = Queue()
        # inpt_send = Queue()
        #
        # p1 = Process(target=sock_work, args=(recv_inpt, inpt_send,))
        # p1.start()
        #
        # while True:
        #
        #     recvinpt = recv_inpt.get()
        #
        #     if recvinpt == 'END':
        #         recv_inpt.close()
        #         inpt_send.close()
        #         print('CLOSE MESSENGER')
        #         break
        #
        #     print('GET:', recvinpt)
        #     if recvinpt:
        #
        #         send = input('ENTER MSG ->') + '\n'
        #         print(send, send, send)
        #
        #         if send.replace('\n', '') == 'ss':
        #             break
        #
        #         inpt_send.put(send)

                # received = None
            # sleep(3)




    except ConnectionRefusedError:
        print('SERVER DID NOT RESPOND')
    except Exception as E:
        raise
    finally:
        sock.close()
        print('THE END')








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




'''

cd PycharmProjects\one_cup_phone
'''