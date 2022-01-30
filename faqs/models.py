from django.db import models

class Faq_Categorie(models.Model):
    id = models.BigAutoField
    name = models.CharField(max_length=255)

class Faq(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Faq_Categorie, on_delete=models.CASCADE, null=False)
    description = models.TextField(null=False)
    created = models.DateTimeField(auto_now=True)