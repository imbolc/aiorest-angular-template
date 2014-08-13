import jinja2
import json

import cfg


def render_string(template, **kwargs):
    template = env.get_template(template)
    return template.render(kwargs)


env = jinja2.Environment(**{
    'loader':      jinja2.FileSystemLoader(cfg.TEMPLATE_PATH),
    'auto_reload': False,

    'block_start_string':   '<%',
    'block_end_string':     '%>',
    'variable_start_string': '<<',
    'variable_end_string':   '>>',
})
env.filters['tojson'] = json.dumps
env.globals.update({
    'cfg': cfg,
})
