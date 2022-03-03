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

    # created_at = models.DateTimeField('created at', default=timezone.now())
    updated_at = models.DateTimeField('updated at', auto_now_add=True)

    # returned = models.BooleanField(False, default="")

    condition = models.CharField(max_length=20, 
                            choices=CONDITION_CHOICES, 
                            default=EXCELLENT)

    def __str__(self):
        return self.laptop_name

    # def __str__(self):
    #     return ("laptop_name: {0}, status: {1}".format(self.laptop_name))



class Lended(models.Model):
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

    lended_laptop_name = models.CharField(max_length=50)
    lendee = models.ForeignKey(User, null=True, unique=False, on_delete=models.CASCADE, related_name="lended_person", )
    lender =  models.CharField(max_length=200, default="Sisekelo Admin")
    lended_at = models.DateTimeField('Date lended', auto_now_add=True)
    serial_number = models.CharField(max_length=50, null=False)
    lending_condition = models.CharField(max_length=20,
                                        choices=CONDITION_CHOICES,
                                        default=EXCELLENT)

    def __str__(self):
        return self.lended_laptop_name

class Returned_laptop(models.Model):
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

    returned_name = models.ForeignKey(Device, related_name="laptopname", on_delete=models.CASCADE)
    any_problem = models.TextField(max_length=200, null=True, blank=True)
    # responsible_party = models.CharField(max_length=100, null=True, blank=True, default="Sisekelo")
    make = models.CharField(max_length=200, null=False)
    serial_number = models.CharField(max_length=50, null=False)
    color = models.CharField(max_length=50, null=True)
    returned_at = models.DateTimeField('Date lended',auto_now_add=True)
    # created_at = models.DateTimeField('created at', default=timezone.now())
    # updated_at = models.DateTimeField('updated at', auto_now_add=True)
    lended_person = models.ForeignKey(Lended, null=True, unique=False, on_delete=models.CASCADE, related_name="lended_person", )
    # lender = models.ForeignKey(Lended, null=True, on_delete=models.CASCADE, blank=True, unique=False, default="Sisekelo")
    # returned = models.BooleanField(False, default="")
    # lended_at = models.DateTimeField('Date lended', auto_now_add=True)

    return_condition = models.CharField(max_length=20,
                            choices=CONDITION_CHOICES, 
                            default=EXCELLENT)

    def __str__(self):
        return self.returned_name

