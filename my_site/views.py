from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your views here.


def get_home_page(request):
    data = {
        'resources': ['posts'],
        'url_names': ['posts-name']
    }
    return render(request, 'home/index.html', context=data)
