import logging
import os

def setup_logging():
    basedir = os.path.dirname(__file__)
    path = os.path.join(basedir, 'log.txt')


    logging.basicConfig(
        filename=path,
        filemode='w',
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%H:%M:%S"
    )

def log_info(msg):
    logging.info(msg)
    print(msg)

def log_warning(msg):
    logging.warning(msg)
    print(msg)

def log_error(msg):
    logging.error(msg)
    print(msg)

def log_debug(msg):
    logging.debug(msg)
    print(msg)
