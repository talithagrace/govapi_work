from django.urls import path
from . import blog_views

urlpatterns = [
    path('', blog_views.searchlist),
]
