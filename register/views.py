from django.shortcuts import render

def register_form(request):
	return render(request,'html/register.html')
