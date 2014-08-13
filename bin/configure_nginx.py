#!var/env/bin/python
import os

from setup import ROOT
import cfg
import lib.os
import lib.fs


with lib.os.root_required():
    fname = '/etc/nginx/sites-enabled/%s' % cfg.HOST
    template = lib.fs.read_file_text('cfg/nginx.txt')
    content = template % {'root': ROOT, 'host': cfg.HOST, 'port': cfg.PORT}
    lib.fs.write_file_text(fname, content)
    print('Nginx config created:', fname)
    os.system('/etc/init.d/nginx configtest && sudo /etc/init.d/nginx restart')
