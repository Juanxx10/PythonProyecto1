from django.shortcuts import render
from datetime import datetime

def index(request):
    context = {
        'mensaje': 'Bienvenidos a mi aplicación Django',
        'year': datetime.now().year
    }
    return render(request, 'myapp/index.html', context)