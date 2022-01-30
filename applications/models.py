from django.db import models
from courses.models import Learnership

# class Highest_qualification(models.Model):
#     # id = models.BigAutoField
#     # enabled = models.BooleanField(default=True)
#     qualification_number = models.IntegerField(auto_created=True, default=0)
#     qualification = models.CharField(max_length=255)

class Qualification(models.Model):
    # qualification_number = models.IntegerField(auto_created=True, default=0)
    qualification = models.CharField(max_length=255)


class Application(models.Model):
    HIGHEST_QUALIFICATION = (
        ('Matric', 'Matric'),
        ('Degree', 'Degree'),
        ('National Diploma', 'National Diploma'),
        )
    ACCREDITED_TYPE = (
        ('Learnership', 'Learnership'),
        ('Short Courses', 'Short Courses'),
        ('Skills Program', 'Skills Program'),
        ('Work Readiness Program', 'Work Readiness Program'),
        ('Financial Literacy', 'Financial Literacy'),
        ('Data Science & Python', 'Data Science & Python'),
        ('Digital Immersion Program', 'Digital Immersion Program'),
        ('Specialized Development Program', 'Specialized Development Program'),
        ('Animation Program', 'Animation Program'),
     )
    EQUITY = (
        ('B', 'Black'),
        ('C', 'Colored'),
        ('I', 'Indian'),
        ('W', 'White'),
        ('O', 'Other'),
     )
    DISABILITY = (
        ('yes', 'Yes'),
        ('no', 'No'),
     )
    CITIZEN = (
        ('yes', 'Yes'),
        ('asylum', 'Asylum'),
        ('visa', 'Visa'),
     )

    course = models.CharField(max_length=50, choices=ACCREDITED_TYPE, default='Learnership')
    # course = models.ForeignKey(Learnership, on_delete=models.CASCADE, null=True)
    # course = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    mid_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    equity = models.CharField(max_length=30, choices=EQUITY, default='B')
    disability = models.CharField(max_length=30, choices=DISABILITY, null=True)
    if_yes_specify = models.TextField(null=True)
    street_address = models.CharField(max_length=255)
    street_address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=11)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=14)
    whatsapp = models.CharField(max_length=14)
    work_phone = models.CharField(max_length=14)
    south_african_citizen = models.CharField(max_length=30, choices=CITIZEN, null=True)
    non_citizen_docs = models.FileField(upload_to='uploads/non_citizen_docs/')
    qualification  = models.CharField(max_length=50, choices=HIGHEST_QUALIFICATION, default='Matric')
    next_of_keen_name = models.CharField(max_length=255)
    next_of_keen_surname = models.CharField(max_length=255)
    next_of_keen_home_tel = models.CharField(max_length=255)
    next_of_keen_cellphone = models.CharField(max_length=255)
    next_of_keen_email = models.EmailField(null=True)
    name_of_employer = models.CharField(max_length=255)
    comments = models.TextField(null=True)
    agreement = models.CharField(max_length=30, choices=DISABILITY, null=True)

    def __str__(self):
        return self.course
