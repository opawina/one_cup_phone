from os.path import abspath


class DATABASE:

    DB_NAME = abspath('.') + '/dwh/twocups.db'


class LOGGING:

    ENABLED_LOGGING = False
    LOG_FILE = './dwh/log_info.log'


class HOST:

    IP = '127.0.0.1'
    PORT = '7777'
