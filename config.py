import os

from dwh import path_to_dwh
path_to_dwh = os.path.dirname(path_to_dwh.__file__).replace('\\', '/')
# import dwh
# path_to_dwh = dwh.__path__.__dict__['_path'][0]



##########################################################################################

            ##########
            # CONFIG #
            ##########


class DATABASE:

    DB_NAME = path_to_dwh + '/twocups.db'


class LOGGING:

    ENABLED_LOGGING = False
    LOG_FILE = './dwh/log_info.log'


class HOST:

    IP = '127.0.0.1'
    PORT = '7777'

##########################################################################################