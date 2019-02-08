from django import forms
from django.contrib.auth.models import User
from main.models import Order

class OrderCreateForm(forms.ModelForm):
	
	#service = forms.CharField(widget=forms.Select(choices=SERVICE_CHOICES))
	#service = forms.ChoiceField(choices=SERVICE_CHOICES)

	class Meta:
		model = Order
		fields = ['service', 'value', 'price', 'place', 'pay_method', 'date_choosen']		

		labels = {			
			'value' : '',
			'price' : ''
		}
		
		widgets = {			
			'price' : forms.TextInput(attrs = {
				'class' : 'myformclass',
				'placeholder' : 'Enter price'}),
		}