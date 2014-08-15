def hello(request):
    name = request.matchdict.get('name', 'world')
    message = 'Hello, {}!'.format(name)
    return {'message': message}
