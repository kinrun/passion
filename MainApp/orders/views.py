from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from main.models import Order
from .forms import OrderCreateForm

import grl

def new_order(request, seller_id):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:        
        form = OrderCreateForm(request.POST) 
        
        # check whether it's valid:
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.buyer = request.user;            
            new_order.seller = User.objects.get(id=seller_id)
            new_order.save()

            #data = {'new_user': new_user}
            #return render(request, 'personal/index.html', data)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/main/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = OrderCreateForm()        
        seller_name = User.objects.get(id=seller_id).username

        balance_btc = request.user.profile.balance_btc
        balance_eth = request.user.profile.balance_eth        
        balance_usd = grl.bal_usd(balance_btc, balance_eth)

        data = {
            'form': form,
            'seller_name': seller_name,
            'balance_btc': balance_btc, 
            'balance_eth': balance_eth, 
            'balance_usd': balance_usd,
            }

        return render(request, 'orders/new_order_index.html', data)

# need to rework for some type of home page for orders
def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:        
        form = OrderCreateForm(request.POST)        
        # check whether it's valid:
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.buyer = request.user;
            #request.session
            new_order.seller = User.objects.get(id=1)
            new_order.save()

            #data = {'new_user': new_user}
            #return render(request, 'personal/index.html', data)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/main/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = OrderCreateForm()
        #seller = User.objects.get(id=1)
        return render(request, 'orders/new_order_index.html', {'form': form})

def my_orders(request):
    list_orders_buy = Order.objects.filter(buyer__exact=request.user)
    number_orders_buy = Order.objects.filter(buyer__exact=request.user).count()
    list_orders_sell = Order.objects.filter(seller__exact=request.user)
    number_orders_sell = Order.objects.filter(seller__exact=request.user).count()
    data = {
        'list_orders_buy': list_orders_buy, 
        'list_orders_sell': list_orders_sell,
        'number_orders_buy': number_orders_buy, 
        'number_orders_sell': number_orders_sell,
        }
    return render(request, 'orders/my_orders_index.html', data)