from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
# Create your views here.


def main_page(request):
    return render(request, 'blog/index.html')


def posts(request):
    return render(request, 'blog/list_detail.html')


def get_info_about_posts_int(request, post):
    data = {
        'number': post
    }
    return render(request, 'blog/detail_by_number.html', context=data)
    # return HttpResponse(f'Info about post with number #{post}')


def get_info_about_posts_str(request, post):
    data = {
        'name': post
    }
    return render(request, 'blog/detail_by_name.html', context=data)
    # return HttpResponse(f'Info about post {post}')

