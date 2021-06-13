import logging
import traceback

from config import config

logging.basicConfig(filename=config.log_file_path,
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)


def info(msg):
    logging.info(msg)


def debug(msg):
    logging.debug(msg)


def error(msg):
    logging.error(msg)


def exception(exc: Exception, msg='', info_level=False):
    if info_level:
        logging.info(f"{format_exc(exc)}\n{traceback.format_exc()}")
    else:
        logging.error(f"{msg}\t{exc.__repr__()}")
        logging.exception(exc)


def format_exc(e: Exception):
    return f"{type(e).__name__}: {e}"
