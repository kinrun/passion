from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
#from django.http import HttpResponse
from .forms import SignInForm


def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        
        form = SignInForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        account = authenticate(request, username=username, password=password)

        if account is not None:
            login(request, account)
            # Redirect to a success page.
            return HttpResponseRedirect('/main/')
        else:
            # Return an 'invalid login' error message.
            return HttpResponseRedirect('/signin/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignInForm()
        return render(request, 'signin/index.html', {'form': form})