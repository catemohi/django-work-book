from django.contrib import admin
from django.urls import path
from django.urls import include 
from django.urls import register_converter 

from . import path_converters
from . import views

register_converter(path_converters.LineConverter, 'line')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('<int:value>', views.params_int),
    path('<line:value>', views.params_line),
    path('<uuid:value>', views.params_uuid),
    path('<slug:value>', views.params_slug),
    path('<str:value>', views.params_str),
]
