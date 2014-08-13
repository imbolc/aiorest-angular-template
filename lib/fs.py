import os
import logging


log = logging.getLogger(__name__)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_file_text(filename, encoding='utf-8'):
    with open(filename, encoding=encoding) as f:
        return f.read()


def write_file_text(filename, text, encoding='utf-8'):
    with open(filename, 'w', encoding=encoding) as f:
        return f.write(text)


def update_file(filename, content):
    saved_content = None
    if os.path.exists(filename):
        saved_content = read_file_text(filename)
    if content == saved_content:
        log.debug('File has not changed: %s', filename)
    else:
        write_file_text(filename, content)
        log.debug('File updated: %s', filename)
