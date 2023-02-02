from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from faker import Faker
# Create your views here.


def posts(request):
    fake = Faker()
    data = {
        'city': [],
        'company': [],
        'date': [],
        'content': [],
        'zipped_all': []
    }

    for _ in range(7):
        data['city'].append(fake.city())
        data['company'].append(fake.company())
        data['date'].append(fake.date())
        data['content'].append(fake.paragraph())
    data['zipped_all'].extend(zip(data['city'], data['company'], data['date'], data['content']))

    return render(request, 'blog/list_detail.html', context=data)


def get_info_about_posts_int(request, post):
    data = {
        'number': post
    }
    return render(request, 'blog/detail_by_number.html', context=data)


def get_info_about_posts_str(request, post):
    data = {
        'name': post
    }
    return render(request, 'blog/detail_by_name.html', context=data)
