from django.core.exceptions import MiddlewareNotUsed
from django.http import HttpResponseServerError


class MyFirstPracticMiddleware:

    def __init__(self, next):
        self.next = next

    def __call__(self, request):
        print('Run logic __call__ method my first middleware before view')
        response = self.next(request)
        print('Run logic __call__ method my first middleware after view')
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print(f'MyFirstPracticMiddleware.process_view say: Choise view - {view_func.__name__}')

    def process_template_response(self, request, response):
        print('process_template_response run')
        response.context_data['input_middleware'] = 'Текст который будет на странице!'
        return response


class MySecondPracticMiddleware:

    def __init__(self, next):
        self.next = next

    def __call__(self, request):
        print('Run logic __call__ method my second middleware before view')
        response = self.next(request)
        print('Run logic __call__ method my second middleware after view')
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print(f'MySecondPracticMiddleware.process_view say: Choise view - {view_func.__name__}')

    def process_exception(self, request, exception):
        print(f'Exception - {exception}')
        return HttpResponseServerError('Server Error!')


class MyLastPracticMiddleware:

    def __init__(self, next):
        self.next = next
        raise MiddlewareNotUsed

    def __call__(self, request):
        print('Run logic __call__ method my last middleware before view')
        response = self.next(request)
        print('Run logic __call__ method my last middleware after view')
        return response
