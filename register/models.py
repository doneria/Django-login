from django.db import models
from django import forms

class USER(models.Model):
	FirstName=models.CharField(max_length=30)
	LastName=models.CharField(max_length=30)
	Email=models.EmailField(max_length=70)
	Password=models.CharField(max_length=30)
	DOB=models.DateField()


