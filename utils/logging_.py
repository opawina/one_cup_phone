'''
TODO:
- хз как достать имя ф вызвавшую данную ф
'''


import logging

from config import LOGGING


logging.basicConfig(
    filename=LOGGING.LOG_FILE,
    filemode='a',
    format=u'[%(asctime)s] %(message)s',
    level=logging.INFO
)

def log(func_in):

    def wrap(*args, **kwargs):

        if LOGGING.ENABLED_LOGGING:
            # хз как достать имя ф вызвавшую данную ф
            logging.info('Function {0} was called by %(module)s'.format(func_in.__name__))
        return func_in(*args, **kwargs)

    return wrap
