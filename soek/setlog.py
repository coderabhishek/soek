import logging

logger = logging.getLogger('Spider')


def setuplogger():
    # setting format of log
    formatter = logging.Formatter('%(message)s')
    logger.setLevel(logging.DEBUG)
    # file location
    debug_log = 'log.txt'

    # adding handler for console logs
    sh = logging.StreamHandler()
    sh.setFormatter(formatter)
    logger.addHandler(sh)

    # adding handler for file logs
    fh = logging.FileHandler(debug_log)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    logger.debug('SETLOG logger setup done')


setuplogger()
