from django.shortcuts import render

def index(request):
    return render(request, '../templates/index.html')

def articles(request):
    return render(request, '../templates/articles/list.html')