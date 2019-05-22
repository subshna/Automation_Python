import logging

logging.basicConfig(filename='../Results_Log/test.log',
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y : %H:%M:%S %p')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug('This is debug message')
logger.info('This is info message')
logger.error('This is error message')
logger.warning('This is warning message')
logger.critical('This is critical message')