#!/usr/bin/env python3
import os

import setup  # noqa
import cfg


try:
    os.makedirs(cfg.ENV_DIR)
except OSError:
    pass
os.system('pyvenv %s' % cfg.ENV_DIR)
os.system('%s/bin/easy_install pip' % cfg.ENV_DIR)
os.system('%s/bin/pip install -r cfg/pipreq.txt' % cfg.ENV_DIR)
