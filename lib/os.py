import os
import sys
import pwd
import contextlib


@contextlib.contextmanager
def root_required():
    username = pwd.getpwuid(os.getuid())[0]
    if username != 'root':
        print('You have to run this script as root')
        sys.exit(1)
    yield
