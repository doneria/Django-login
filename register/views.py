from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.urls import reverse
from register.forms import RegistrationForm

class register_form(TemplateView):

	def get(self,request):
		form=RegistrationForm()
		return render(request,'html/register.html',{'form': form})


	def post(self,request):
		form=RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			text=form.cleaned_data['FirstName']
			form=RegistrationForm()
			

		args={'form':form, 'text':text}	
		return render(request,'html/register.html',args)

