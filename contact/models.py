from django.db import models


class Contact(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField(null=True)
	cell = models.CharField(max_length=255)
	message = models.TextField(null=True)
	date_created = models.DateTimeField(auto_now=True)


class Enquiry(models.Model):
	full_name = models.CharField(max_length=255)
	email = models.EmailField(null=True)
	cell = models.CharField(max_length=255)
	program_of_interest = models.CharField(max_length=255)
	message = models.TextField(null=True)
	date_created = models.DateTimeField(auto_now=True)