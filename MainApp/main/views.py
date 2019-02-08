from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

def index(request):	
	data = {'asd': 'asd'}
	return render(request, 'main/index.html', data)

def log_out(request):
	logout(request)	
	return HttpResponseRedirect('/signin/')
	