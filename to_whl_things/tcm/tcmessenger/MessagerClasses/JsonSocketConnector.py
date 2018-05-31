import json
import socket

from utils.logging_ import log


msg_tmpl_client = {
        # 'authorization': {
        #     'action': 'authorization',
        #     'new_user': False,
        #     'login': 'login',
        #     'passw': 'passw'
        # },
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

    # @log
    def __init__(self):

        self.data = None


    # @log
    def json_to_bytes(self):

        data = json.dumps(self.data) + '\n'
        data = data.encode()

        return data


    # @log
    def bytes_to_json(self, bmsg):

        data = bmsg.decode().replace('\n', '')
        data = json.loads(data)

        return data


    def tmpl_authorization(self, user_data):

        self.data = {
            'action': 'authorization',
            'new_user': user_data['new_user'], # bool
            'login': user_data['login'],
            'passw': user_data['passw']
        }

        return self.json_to_bytes()











'''

cd PycharmProjects\one_cup_phone
'''
