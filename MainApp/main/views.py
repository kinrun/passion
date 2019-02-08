from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

# for coin market
import json 
import requests 

def index(request):
	#getting current data about bitcoin and taking price from it
	r = requests.get('https://api.coinmarketcap.com/v1/ticker/bitcoin/')
	# price_usd have a lot of numbers after .
	price_usd = float(r.json()[0]['price_usd'])
	# decreased to 2 numbers after .
	btc = float("{0:.2f}".format(price_usd))	
	#getting current data about ethereum and taking price from it
	r = requests.get('https://api.coinmarketcap.com/v1/ticker/ethereum/')
	# price_usd have a lot of numbers after .
	price_usd = float(r.json()[0]['price_usd'])
	# decreased to 2 numbers after .
	eth = float("{0:.2f}".format(price_usd))
	
	data = {'btc': btc, 'eth': eth}
	return render(request, 'main/index.html', data)

def log_out(request):
	logout(request)	
	return HttpResponseRedirect('/signin/')
	