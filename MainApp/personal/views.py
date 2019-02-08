from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import NewProfileForm
import grl

def index(request):
	if request.user.is_authenticated:
		# Do something for authenticated users
		balance_btc = request.user.profile.balance_btc
		balance_eth = request.user.profile.balance_eth	
		balance_usd = grl.bal_usd(balance_btc, balance_eth)
		data = {
			'content': 'personal/content.html', 
			'username': request.user.username, 
			'balance_btc': balance_btc,
			'balance_eth': balance_eth, 
			'balance_usd': balance_usd,
			}
		return render(request, 'MainApp/core.html', data)
	else:
		return HttpResponseRedirect('/signin/')


def newuser(request):
	if request.user.is_authenticated:
		# Do something for authenticated users
		# if this is a POST request we need to process the form data
		if request.method == 'POST':
			# create a form instance and populate it with data from the request:        
			form = NewProfileForm(request.POST)			
			# check whether it's valid:
			if form.is_valid():
				user = User.objects.get(username = request.user.username)
				user.first_name = form.cleaned_data['first_name']
				user.last_name = form.cleaned_data['last_name']
				user.profile.country = form.cleaned_data['country']
				user.profile.city = form.cleaned_data['city']
				user.save()
				return HttpResponseRedirect('/main/')
		else:
			form = NewProfileForm()			
			data = {'content': 'newuser/content.html', 'form': form}
			return render(request, 'MainApp/core.html', data)
	

	else:
		return HttpResponseRedirect('/signin/')