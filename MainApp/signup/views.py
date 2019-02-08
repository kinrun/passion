from django.shortcuts import render

from django.http import HttpResponseRedirect
#from django.http import HttpResponse
from .forms import SignUpForm


def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignUpForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()

            #data = {'new_user': new_user}
            #return render(request, 'personal/index.html', data)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/signin/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignUpForm()
        return render(request, 'signup/index.html', {'form': form})