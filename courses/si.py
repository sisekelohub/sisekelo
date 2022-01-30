from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# from inventory.user.models import Lendee


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

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, null=True, blank=True)
    responsible_party = models.CharField(max_length=100, null=True, blank=True)
    make = models.CharField(max_length=200, null=False)
    # purchased_at = models.DateTimeField('Date purchased', default=timezone.now())
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    lendee = models.ForeignKey(User, null=True, blank=True, unique=False, on_delete=models.CASCADE)
    lender = models.ForeignKey(User, null=True, blank=True, unique=False, on_delete=models.CASCADE)
    condition = models.CharField(max_length=2, choices=CONDITION_CHOICES, default=EXCELLENT)

   
    def get_status_color(self):
        '''Return a css color that corresponds to the device's status.
        '''
        if self.status in [Device.CHECKED_IN_NOT_READY,
                            Device.BROKEN]:
            return 'red'
        elif self.status in [Device.CHECKED_IN_READY, Device.CHECKED_IN]:
            return 'green'
        elif self.status in [Device.CHECKED_OUT]:
            return '#ffcc00'

