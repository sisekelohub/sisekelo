from django.db import models


class Event(models.Model):
    MODE_OF_DELIVERY = (
        ('O', 'Online'),
        ('P', 'Physical'),
        ('H', 'Hybrid'),
    )

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=255)
    mode= models.CharField(max_length=1, choices=MODE_OF_DELIVERY)
    address = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date = models.DateTimeField(blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')


    def __str__(self):
        return self.title

