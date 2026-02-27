import logging
import os

test_mode = True

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, '..', 'logs')
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, 'main_log.txt')



if test_mode:
    logging.basicConfig(filename=LOG_FILE,
                        filemode='w',
                        format='[%(asctime)s] [%(levelname)s] %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.DEBUG)

else:
    logging.disable(logging.CRITICAL)

def log_info(txt):
    print(txt)
    logging.info(txt)

def log_debug(txt):
    print(txt)
    logging.debug(txt)

def log_warning(txt):
    print(txt)
    logging.warning(txt)

def log_error(txt):
    print(txt)
    logging.error(txt)

def log_critical(txt):
    print(txt)
    logging.critical(txt)