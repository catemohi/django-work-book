class TestConverter:

    regx = r'[0-9]' #регулярное выражение для поиска последовательности в строке

    def to_python(self, value: str):
        # Метод для преобразования строки из пути в обьект python
        # raise ValueError - вызывается если строка не подходит нам.
        return value

    def to_string(self, value: str):
        # Обратное преобразование обьекта python в строку
        # используется функцией django.urls.reverse или тегом url
        return value

