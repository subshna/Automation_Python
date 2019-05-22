import logging

logging.basicConfig(filename='../Results_Log/test.log',
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y : %H:%M:%S %p',
                    level=logging.DEBUG)

logging.debug('This is debug message')
logging.info('This is info message')
logging.error('This is error message')
logging.warning('This is warning message')
logging.critical('This is critical message')