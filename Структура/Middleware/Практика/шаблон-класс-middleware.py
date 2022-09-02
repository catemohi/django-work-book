class MyMiddleware:

    def __init__(self, next):
        """Инициализация middleware

        Args:
            next: либо следующий middleware или view.
        """
        self.next = next 
        # Здесь можно вставлять дополнительные инициализации

    def __call__(self, request):
        # Здесь выполняется обработка клиентского запроса
        # ...
        # ...
        # ...
        response = self.next(request)
        # Здесь выполняется обработка ответа от view
        # ...
        # ...
        # ...
        return response
