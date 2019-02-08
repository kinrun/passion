from django.shortcuts import render

def index(request):
    data = {'mark1': 'trust'}
    return render(request, 'appartaments/index.html', data)