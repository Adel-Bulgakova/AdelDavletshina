# encoding: utf-8
from django.shortcuts import render

def about(request):
    return render(request, "home/home.html")

