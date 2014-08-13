#!var/env/bin/python
import asyncio
import aiorest

import cfg
import lib.logging
import prepare_static
import urls


lib.logging.setup(cfg.LOG_FILE)
prepare_static.client_config(urls=urls.CLIENT_URLS)
prepare_static.render_html('index.html')


server = aiorest.RESTServer(hostname='127.0.0.1')
for url in urls.SERVER_URLS:
    server.add_url(*url)


loop = asyncio.get_event_loop()
loop.run_until_complete(loop.create_server(
    server.make_handler, '127.0.0.1', cfg.PORT))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
