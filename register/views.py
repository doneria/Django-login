from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.urls import reverse
from register.forms import RegistrationForm
from register.models import USER
from django import forms
from django.http import HttpResponse

class register_form(TemplateView):

	def get(self,request):
		form=RegistrationForm()
		return render(request,'html/register.html',{'form': form})


	def post(self,request):
		form=RegistrationForm(request.POST)
		if form.is_valid():
			userObj=form.cleaned_data
			email=userObj['Email']
			password=userObj['Password']
			text=''
			if not(USER.objects.filter(Email=email).exists() or USER.objects.filter(Password=password)):
				form.save()
			else:
				return HttpResponse('Looks like a username with that email or password already exists')
		
		else:
			form=RegistrationForm()



		args={'form':form,'text':text}	
		return render(request,'html/register.html',args)

