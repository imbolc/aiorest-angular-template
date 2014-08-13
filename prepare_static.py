import os

import lib.fs
import lib.jinja


def client_config(**config):
    content = lib.jinja.render_string('client_config.js', config=config)
    lib.fs.update_file('client/cfg.svc.js', content)


def render_html(*templates):
    for template in templates:
        html = lib.jinja.render_string(template)
        filename = os.path.join('static', 'build', template)
        lib.fs.update_file(filename, html)
