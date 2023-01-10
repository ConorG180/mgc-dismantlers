from django.shortcuts import render
from django.http import HttpResponse


def render_homepage(request):
    return render(request, 'home/index.html',)