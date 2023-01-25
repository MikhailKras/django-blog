from django.urls import path
from . import views

urlpatterns = [
    path('<int:post>', views.get_info_about_posts_int),
    path('<str:post>', views.get_info_about_posts_str),
]
