from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# from pytz import unicode


class Device(models.Model):
    '''An abstract device model.
    '''
    # These constants define choices for a device's status
    CHECKED_IN = 'CI'
    CHECKED_IN_READY = 'IR'
    CHECKED_IN_NOT_READY = 'IN'
    CHECKED_OUT = 'CO'
    STORAGE = 'ST'
    BROKEN = 'BR'
    MISSING = 'MI'
    SENT_FOR_REPAIR = 'RE'

    # Other constants for condition
    EXCELLENT = 'EX'
    SCRATCHED = 'SC'

    # Define possible choices for condition field
    CONDITION_CHOICES = (
        (EXCELLENT, 'Excellent'),
        (SCRATCHED, 'Scratched'),
        (BROKEN, 'Broken'),
        (MISSING, 'Missing'),
    )

    laptop_name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, null=True, blank=True)
    responsible_party = models.CharField(max_length=100, null=True, blank=True, default="Sisekelo")
    make = models.CharField(max_length=200, null=False)
    serial_number = models.CharField(max_length=50, null=False)
    color = models.CharField(max_length=50, null=True)
    lended_at = models.DateTimeField('Date lended',auto_now_add=True)
    # created_at = models.DateTimeField('created at', default=timezone.now())
    updated_at = models.DateTimeField('updated at', auto_now_add=True)
    lendee = models.ForeignKey(User, null=True, unique=False, on_delete=models.CASCADE, related_name="lendee", )
    lender = models.ForeignKey(User, null=True, on_delete=models.CASCADE, blank=True, unique=False, default="Sisekelo")

    condition = models.CharField(max_length=20, 
                            choices=CONDITION_CHOICES, 
                            default=EXCELLENT)

    def __str__(self):
        return ("name: {0}, status: {1}".format(self.name, self.status))


  