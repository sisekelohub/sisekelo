from django.db import models
from django.contrib.auth.models import User
import string
import random
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

length = 6

all = string.ascii_uppercase + string.digits
password = "".join(random.sample(all,length))


class Profile(models.Model):
    GENDER_CHOICES = (
        ('1', 'Female'),
        ('2', 'Male'),
        ('3', 'Prefer Not To Say'),
        ('4', 'Other'),
        )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    student_id = models.CharField(max_length=32, default=f"2022-{password}")
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    gender   = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True, blank=True, default=1)
    address  = models.CharField(max_length=255, null=True, blank=True)
    city     = models.CharField(max_length=50, null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()




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


# class Profile(models.Model):
#     GENDER_CHOICES = (
#         ('1', 'Female'),
#         ('2', 'Male'),
#         ('3', 'Prefer Not To Say'),
#         ('4', 'Other'),
#         )

#     # Managed fields
#     user     = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
#     student_id = models.CharField(max_length=32, default=f"2022-{password}")
#     # avatar   = models.ImageField(upload_to="profile_images", null=True, blank=True)
#     avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
#     bio = models.TextField()
#     birthday = models.DateField(null=True, blank=True)
#     gender   = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True, blank=True, default=1)
#     phone    = models.CharField(max_length=32, null=True, blank=True)
#     address  = models.CharField(max_length=255, null=True, blank=True)
#     number   = models.CharField(max_length=32, null=True, blank=True)
#     city     = models.CharField(max_length=50, null=True, blank=True)
#     # zip      = models.CharField(max_length=30, null=True, blank=True)

#     def __str__(self):
#         return self.user.username


    # @property
    # def get_avatar(self):
    #     return self.avatar.url if self.avatar else static('assets/img/team/default-profile-picture.png')


# from django.db import models
# # from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# class Profile(models.Model):
#     GENDER_CHOICES = (
#         ('1', 'Female'),
#         ('2', 'Male'),
#         ('3', 'Prefer Not To Say'),
#         ('4', 'Other'),
#         )
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
#     bio = models.TextField(max_length=500, blank=True)
#     email_confirmed = models.BooleanField(default=False)
#     location = models.CharField(max_length=30, blank=True)
#     birth_date = models.DateField(null=True, blank=True)
#     student_id = models.CharField(max_length=32, default=f"2022-{password}")
#     # avatar   = models.ImageField(upload_to="profile_images", null=True, blank=True)
#     avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
#     # bio = models.TextField()
#     birthday = models.DateField(null=True, blank=True)
#     gender   = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True, blank=True, default=1)
#     phone    = models.CharField(max_length=32, null=True, blank=True)
#     address  = models.CharField(max_length=255, null=True, blank=True)
#     number   = models.CharField(max_length=32, null=True, blank=True)
#     city     = models.CharField(max_length=50, null=True, blank=True)

# # @receiver(post_save, sender=User)
# # def update_user_profile(sender, instance, created, **kwargs):
# #     if created:
# #         Profile.objects.create(user=instance)
# #     instance.profile.save()