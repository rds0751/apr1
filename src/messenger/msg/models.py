from django.db import models

from django.contrib.auth.models import User

class message(models.Model):
	content=models.CharField(max_length=500)
	date=models.DateTimeField()
	


class call(models.Model):
	calltime = models.DateTimeField(default=now)
	caller = models.CharField(max_length=33)
