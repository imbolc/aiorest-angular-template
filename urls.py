import handlers


SERVER_URLS = [
    ('GET', '/hello',        handlers.hello),
    ('GET', '/hello/{name}', handlers.hello),
]

CLIENT_URLS = {
    'hello': '/api/hello/:name',
}
