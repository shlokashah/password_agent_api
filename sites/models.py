from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# Create your models here.

class Sites(models.Model):
	website = models.CharField(max_length=100)
	username = models.CharField(max_length=256)
	password = models.CharField(max_length=256)
	user = models.ForeignKey(User,default=None,on_delete=models.PROTECT)
	def __str__(self):
		return self.website
 
	
	
