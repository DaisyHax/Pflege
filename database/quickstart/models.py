from django.db import models

class Pflege(models.Model):
	date = models.CharField(max_length=15)
	time = models.CharField(max_length=15)
	reciever = models.CharField(max_length=100)
	content = models.CharField(max_length=3000)
