from django import forms
from django.contrib.auth.models import User
from main.models import Profile

class NewProfileForm(forms.ModelForm):
	
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=30)
	#service = forms.CharField(widget=forms.Select(choices=SERVICE_CHOICES))
	#service = forms.ChoiceField(choices=SERVICE_CHOICES)

	class Meta:
		model = Profile
		fields = ['country', 'city']		

		labels = {			
			'country' : '',
			'city' : ''
		}
		
		widgets = {			
			'country' : forms.TextInput(attrs = {
				'class' : 'myformclass',
				'placeholder' : 'Enter country'}),
			'city' : forms.TextInput(attrs = {
				'class' : 'myformclass',
				'placeholder' : 'Enter city'}),
		}