from django.shortcuts import render

def index(request):
	if request.user.is_authenticated:
		# Do something for authenticated users.
		data = {'username': request.user.username}
		return render(request, 'personal/index.html', data)
	else:
		# Do something for anonymous users.
		data = {'username': 'Log In'}
		return render(request, 'personal/index.html', data)