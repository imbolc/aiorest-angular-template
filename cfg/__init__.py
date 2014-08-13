DEBUG = False
HOST, PORT = 'aio-angular.l.com', 8765
LOG_FILE = 'var/log/site.log'
TEMPLATE_PATH = 'templates'
ENV_DIR = 'var/env'

try:
    from cfg.local import *  # noqa
except ImportError:
    pass
