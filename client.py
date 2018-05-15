#!/usr/bin/env python3
'''
Beautiful code!
'''

from MessagerClasses.CClient import Client
from utils.cli_handler import cli_handler
from utils.logging import log

@log
def main():

    socket_ = cli_handler()
    with Client(socket_) as sockk:

        # общаемся
        while True:
            try:
                recv_data = sockk.recv_()
                print('RECIVE:', recv_data['message'])
            except:
                pass
            finally:
                inpt = input()
                sockk.json_tmpl['message'] = inpt
                sockk.send_()

                if inpt == 'ss':
                    break
    # явно не закрываем соединеие т.к. используется менеджер контекста






if __name__ == '__main__':
    main()



'''

cd PycharmProjects\one_cup_phone
'''