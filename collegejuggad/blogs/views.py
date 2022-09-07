from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html', {'y': [1, 2, 3], 'm': "hhh"})


def post(request):
    return render(request, 'single-news.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def blog_write(request):
    return render(request, 'blog_write.html')
