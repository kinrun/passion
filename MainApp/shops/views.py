from django.shortcuts import render

def index(request):
    data = {'mark1': 'trust'}
    return render(request, 'shops/index.html', data)