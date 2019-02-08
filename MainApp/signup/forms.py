from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password']

		labels = {
			'username' : '',
			'email' : '',
			'password' : ''
		}
		
		widgets = {
			'username' : forms.TextInput(attrs = {
				'class' : 'myfieldclass', 
				'placeholder' : 'Enter your username'}),
			'email' : forms.TextInput(attrs = {
				'class' : 'myfieldclass', 
				'placeholder' : 'E-mail'}),
			'password' : forms.TextInput(attrs = {
				'class' : 'myfieldclass', 
				'placeholder' : 'Password'}),
		}

	def clean(self):
		return self.cleaned_data

	def clean_password(self):
		password = self.cleaned_data.get('password')
		return password

	def clean_username(self):
		# Get the username
		username = self.cleaned_data.get('username')

		# Check to see if any users already exist with this username.
		if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
			raise forms.ValidationError(u'Username "%s" is already in use.' % username)
		return username

	def clean_email(self):
		# Get the email
		email = self.cleaned_data.get('email')

		# Check to see if any users already exist with this email as a username.
		try:
			match = User.objects.get(email=email)
		except User.DoesNotExist:
			# Unable to find a user, this is fine
			return email

		# A user was found with this as a username, raise an error.
		raise forms.ValidationError(u'Email address "%s" is already in use.' % email)