from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

# Will be the Welcome page
def index(request):
	if request.user.is_authenticated:
		data = {'content': 'main/content.html'}
		return render(request, 'MainApp/core.html', data)
	else:
		return HttpResponseRedirect('/signin/')

# Will be showed list of best sellers
def sellers(request):
	if request.user.is_authenticated:
		data = {'content': 'sellers/content.html'}
		return render(request, 'MainApp/core.html', data)
	else:
		return HttpResponseRedirect('/signin/')
	
# Will be showed list of best saloons
def saloons(request):
	if request.user.is_authenticated:		
		data = {'content': 'saloons/content.html'}
		return render(request, 'MainApp/core.html', data)
	else:
		return HttpResponseRedirect('/signin/')
	
# no need words
def log_out(request):
	logout(request)	
	return HttpResponseRedirect('/signin/')
	