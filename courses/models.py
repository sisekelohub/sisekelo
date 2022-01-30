from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now
from django.urls import reverse


class Nfq(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Program_Catalogue(models.Model):
    name = models.CharField(max_length=100)

    # number = models.IntegerField(null=True)

    def __str__(self):
        return self.name



class Accredited_Program(models.Model):
    ACCREDITED_TYPE = (
        ('Learnership', 'Learnership'),
        ('Short Courses', 'Short Courses'),
        ('Skills Program', 'Skills Program')
        )
    CERTIFICATE_TYPE = (
        ('National Certificate', 'National Certificate'),
        ('Further Education & Training', 'Further Education & Training')
    )
    MODE_OF_DELIVERY = (
        ('Online', 'Online'),
        ('Physical', 'Physical'),
        ('Hybrid', 'Hybrid'),
    )
    TARGET_AUDIENCE = (
        ('Beginner', 'Beginner'),
        ('Upskilling', 'Upskilling'),
        ('Expert', 'Expert'),
    )
    PAYMENT_OPTION = (
        ('EFT', 'EFT'),
        ('CARD', 'CARD'),
        ('BANK TRANSFER', 'BANK TRANSFER'),
    )
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    program_type = models.CharField(max_length=50, choices=ACCREDITED_TYPE, default='Learnership') 
    title = models.CharField(max_length=200)
    certificate_type = models.CharField(max_length=50, choices=CERTIFICATE_TYPE, default='National Certificate')
    description = models.TextField(blank=True, null=True )
    image = models.ImageField(upload_to='uploads/learnership_images/', null=True)
    mode_of_delivery = models.CharField(max_length=10, choices=MODE_OF_DELIVERY)
    target_audiences = models.CharField(max_length=50, choices=TARGET_AUDIENCE, default="Beginner")
    career_prospects = models.TextField(null=False, default="")
    nfq_level = models.ForeignKey(Nfq, on_delete=models.CASCADE, related_name="nfqlevel1", default="1")
    credits = models.IntegerField(null=False, default="130")
    # outcomes = models.TextField(null=False, default="")
    expectations = models.TextField(blank=True)
    modules = models.TextField(null=True, default="")
    price = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    payment_options = models.CharField(max_length=50, choices=PAYMENT_OPTION, default="Beginner")
    # duration = models.DurationField(null=False)
    duration = models.CharField(max_length=50, null=True)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=None)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=None) 
    brochure = models.FileField(upload_to='uploads/learnership_brochures', null=False, default="")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    slug = models.SlugField(max_length=200, primary_key=True, auto_created=False, default = "")
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField (auto_now=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("courses:course_detail", kwargs={"slug": self.slug})


class Specialized_Course(models.Model):
    ACCREDITED_TYPE = (
        ('Work Readiness Program', 'Work Readiness Program'),
        ('Financial Literacy', 'Financial Literacy'),
        ('Data Science & Python', 'Data Science & Python'),
        ('Digital Immersion Program', 'Digital Immersion Program'),
        ('Specialized Development Program', 'Specialized Development Program'),
        ('Animation Program', 'Animation Program'),
        )
    MODE_OF_DELIVERY = (
        ('O', 'Online'),
        ('P', 'Physical'),
        ('H', 'Hybrid'),
    )
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    program_type = models.CharField(max_length=50, choices=ACCREDITED_TYPE, default='Work Readiness Program') 
    title = models.CharField(max_length=200)
    overview = models.TextField(null=False, default="")
    description = models.TextField(blank=False, null=True)
    image = models.ImageField(upload_to='uploads/learnership_images/', null=True)
    mode_of_delivery = models.CharField(max_length=1, choices=MODE_OF_DELIVERY, default='O')
    expectations = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    duration = models.CharField(max_length=50, null=True)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=None)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=None) 
    specialized_brochure = models.FileField(upload_to='uploads/learnership_brochures', null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title


class Learnership(models.Model):
    CERTIFICATE_TYPE = (
        ('National Certificate', 'National Certificate'),
        ('Further Education & Training', 'Further Education & Training')
    )
    MODE_OF_DELIVERY = (
        ('Online', 'Online'),
        ('Physical', 'Physical'),
        ('Hybrid', 'Hybrid'),
    )
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=200)
    certificate_type = models.CharField(max_length=50, choices=CERTIFICATE_TYPE, default='National Certificate')
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='uploads/learnership_images/', null=True)
    mode_of_delivery = models.CharField(max_length=10, choices=MODE_OF_DELIVERY)
    nfq_level = models.ForeignKey(Nfq, on_delete=models.CASCADE, related_name="nfqlevel")
    credits = models.IntegerField(null=False)
    # outcomes = models.TextField(null=False, default="")
    expectations = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    # duration = models.DurationField(null=False)
    duration = models.CharField(max_length=50, null=True)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=None)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=None)
    modules = models.TextField(null=False, default="")
    brochure = models.FileField(upload_to='uploads/learnership_brochures')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    slug = models.SlugField(max_length=200, primary_key=True, auto_created=False, default = "")
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField (auto_now=True)

    def __str__(self):
        return self.title  

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super(Course, self).save(*args, **kwargs)

    
class Short_Course(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    MODE_OF_DELIVERY = (
        ('Online', 'Online'),
        ('Physical', 'Physical'),
        ('Hybrid', 'Hybrid'),
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=False, null=True)
    image = models.ImageField(upload_to='uploads/learnership_images/', null=True)
    mode_of_delivery = models.CharField(max_length=30, choices=MODE_OF_DELIVERY, default='O')
    expectations = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    duration = models.CharField(max_length=50, null=True)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=None)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=None)
    overview = models.TextField(null=False, default="")
    accredited_brochure = models.FileField(upload_to='uploads/learnership_brochures', null=True)
    slug = models.SlugField(max_length=200, primary_key=True, auto_created=False, default = "")
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField (auto_now=True)

    def __str__(self):
        return self.title

# class Skills_Program(models.Model):
#     STATUS_CHOICES = (
#         ('draft', 'Draft'),
#         ('published', 'Published'),
#     )
#     MODE_OF_DELIVERY = (
#         ('O', 'Online'),
#         ('P', 'Physical'),
#         ('H', 'Hybrid'),
#     )
#     title = models.CharField(max_length=200)
#     description = models.TextField(blank=False, null=True)
#     image = models.ImageField(upload_to='uploads/learnership_images/', null=True)
#     mode_of_delivery = models.CharField(max_length=1, choices=MODE_OF_DELIVERY, default='O')
#     expectations = models.TextField(blank=True)
#     price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
#     duration = models.CharField(max_length=50, null=True)
#     start_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=None)
#     end_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=None)
#     overview = models.TextField(null=False, default="")
#     skills_brochure = models.FileField(upload_to='uploads/learnership_brochures', null=True)

#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

#     def __str__(self):
#         return self.title


# class Online(models.Model):
#     title = models.CharField(max_length=200)