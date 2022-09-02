from django.template.response import TemplateResponse 

# Create your views here.
def index(request):
    return TemplateResponse(request, 'practic/index.html', context={'input_middleware': 'Текст который я не увижу!'})