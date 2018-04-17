import logging


logging.basicConfig(
    filename='log_info.log',
    filemode='a',
    format=u'%(asctime)s Function %(funcName)s was called by function %(module)s',
    level=logging.INFO
)
