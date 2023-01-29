from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
# Create your views here.


def main_page(request):
    return render(request, 'blog/index.html')


def posts(request):
    return HttpResponse('<h1>All posts</h1>')


def get_info_about_posts_int(request, post):
    return HttpResponse(f'Info about post with number #{post}')


def get_info_about_posts_str(request, post):
    return HttpResponse(f'Info about post {post}')

