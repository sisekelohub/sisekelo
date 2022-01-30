from django.db import models
from django.contrib.auth.models import User
import string
import random

length = 6

all = string.ascii_uppercase + string.digits
password = "".join(random.sample(all,length))

# print(f"2022-{password}")

# Extending User Model Using a One-To-One Link
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
#     bio = models.TextField()
#     # birthday = models.DateField(null=True, blank=True)
#     # gender   = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True, blank=True)
#     # phone    = models.CharField(max_length=32, null=True, blank=True)
#     # address  = models.CharField(max_length=255, null=True, blank=True)
#     # number   = models.CharField(max_length=32, null=True, blank=True)
#     # city     = models.CharField(max_length=50, null=True, blank=True)
    

#     # @property
#     # def get_avatar(self):
#     #     return self.avatar.url if self.avatar else static('assets/img/team/default-profile-picture.png')

#     def __str__(self):
#         return self.user.username


class Profile(models.Model):
    GENDER_CHOICES = (
        ('1', 'Female'),
        ('2', 'Male'),
        ('3', 'Prefer Not To Say'),
        ('4', 'Other'),
        )

    # Managed fields
    user     = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    student_id = models.CharField(max_length=32, default=f"2022-{password}")
    # avatar   = models.ImageField(upload_to="profile_images", null=True, blank=True)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()
    birthday = models.DateField(null=True, blank=True)
    gender   = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True, blank=True, default=1)
    phone    = models.CharField(max_length=32, null=True, blank=True)
    address  = models.CharField(max_length=255, null=True, blank=True)
    number   = models.CharField(max_length=32, null=True, blank=True)
    city     = models.CharField(max_length=50, null=True, blank=True)
    # zip      = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.user.username


    # @property
    # def get_avatar(self):
    #     return self.avatar.url if self.avatar else static('assets/img/team/default-profile-picture.png')