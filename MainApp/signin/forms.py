from django import forms
from django.contrib.auth.models import User

class SignInForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']

		labels = {
			'username' : '',			
			'password' : ''
		}
		
		widgets = {
			'username' : forms.TextInput(attrs = {
				'class' : 'myfieldclass', 
				'placeholder' : 'Enter your username'}),			
			'password' : forms.TextInput(attrs = {
				'class' : 'myfieldclass', 
				'placeholder' : 'Password'}),
		}