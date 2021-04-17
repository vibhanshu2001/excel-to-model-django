from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True,null=True)
    location = models.CharField(max_length=50, blank=True,null=True)
