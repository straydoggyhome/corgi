import typing


class Corgi:
    def __init__(self):
        # init params
        pass

    def wsgi_app(self, environ: dict, start_response: typing.Callable) -> typing.Any:
        # response = self.full_dispatch_request()

        def response(environ, start_response):
            start_response('200 OK', [('Content-Type', 'text/html')])
            return [b'<h1>Hello, web!</h1>']

        return response(environ, start_response)

    def __call__(self, environ: dict, start_response: typing.Callable) -> typing.Any:
        # __call__ 不直接返回，而是返回 wsgi_app ，好加中间件
        # start_response('200 OK', [('Content-Type', 'text/html')])
        return self.wsgi_app(environ=environ, start_response=start_response)

