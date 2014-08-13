import os
import logging
import logging.handlers


def setup(filename=None, console_level='DEBUG', file_level='ERROR'):
    logging.getLogger('').setLevel(logging.NOTSET)

    # to file
    if filename:
        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))
        file_handler = logging.handlers.RotatingFileHandler(
            filename=filename, mode='a+',
            maxBytes=1000000,
            backupCount=10)
        file_handler.setLevel(getattr(logging, file_level))
        file_handler.setFormatter(
            logging.Formatter('%(asctime)s\t%(levelname)-8s %(message)s',
                              datefmt='%d-%m-%Y %H:%M:%S'))
        logging.getLogger('').addHandler(file_handler)

    # to console
    console = logging.StreamHandler()
    console.setLevel(getattr(logging, console_level))
    console.setFormatter(logging.Formatter('%(levelname)-8s %(message)s'))
    logging.getLogger('').addHandler(console)
