from django.http import HttpResponse
from django.shortcuts import render


def home_page_view(request, *args, **kwargs):
    return render(request, 'home.html', context={'title': 'This is the home page'})
