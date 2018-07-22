from django import forms
from register.models import USER

class RegistrationForm(forms.ModelForm):
	


	class Meta:
		model=USER
		fields=('FirstName','LastName','Email','Password','DOB')




	






