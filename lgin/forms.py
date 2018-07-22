from django import forms

class LoginForm(forms.Form):
	email = forms.EmailField(label='Email')
	password1 = forms.CharField(label='Password',widget=forms.PasswordInput())
	