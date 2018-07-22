from django.shortcuts import render
from lgin.forms import LoginForm
from django.views.generic import TemplateView
from register.models import USER
from django.http import HttpResponse

class login_form(TemplateView):
	def get(self,request):
		form=LoginForm()
		return render(request,'html/main.html',{'form':form})

	
def validate(request):
	try:
		user=USER.objects.get(Email=request.GET['email'])
		password=USER.objects.get(Password=request.GET['password1'])
	except USER.DoesNotExist:
		user=None
		
	if user is not None:
		message='welcome: %r' % request.GET['email']
	else:
		message='please register before loging in'
	return HttpResponse(message)	
		

	

		
		




	
