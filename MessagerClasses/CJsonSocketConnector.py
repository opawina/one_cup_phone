import json
import socket

from utils.logging_ import log


msg_tmpl_client = {
    'new_user': {},
    'authorization': {},
    # 'get_all_users': {},
    # 'add_user_list_contacts': {},
    # 'del_user_list_contacts': {},
    'start_chat_privat': {},
    # 'start_chat_group': {},
    'message': {},
    'exit_chat': {},
    'close_messager': {}
}
msg_tmpl_server = {
    'response': True,
    'sent_all_users': {},
    # 'sent_list_contacts': {},
    'start_chat_privat': {},
    # 'start_chat_group': {},
    'message': {}
}


class JsonSocketConnector:

    @log
    def __init__(self):

        self.sock_main = socket.socket(
            family=socket.AF_INET,
            type=socket.SOCK_STREAM,
            proto=0
        )
        self.socks_write = []
        self.socks_read = []
        self.json_tmpl = {
            "action": None,
            "time": None,
            "message": None
        }


    @log
    def send_(self):

        buf = json.dumps(self.json_tmpl)
        buf = buf.encode()

        self.sock.send(buf)


    @log
    def recv_(self):

        recv_data = self.sock.recv(1024)

        recv_data = recv_data.decode()
        recv_data = json.loads(recv_data)

        return recv_data



'''

cd PycharmProjects\one_cup_phone
'''


