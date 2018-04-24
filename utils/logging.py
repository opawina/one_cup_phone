'''
TODO:
- хз как достать имя ф вызвавшую данную ф
'''


import logging


logging.basicConfig(
    filename='./log_info.log',
    filemode='a',
    format=u'[%(asctime)s] %(message)s',
    level=logging.INFO
)

def log(func_in):

    def wrap(*args, **kwargs):

        # хз как достать имя ф вызвавшую данную ф
        logging.info('Function {0} was called by %(module)s'.format(func_in.__name__))
        return func_in(*args, **kwargs)

    return wrap
