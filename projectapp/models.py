from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True,null=True)
    location = models.CharField(max_length=50, blank=True,null=True)
class FileUpload(models.Model):
    sheetname = models.CharField(max_length=50, blank=True, null=True)
    fileupload = models.FileField()
    date = models.DateTimeField(default=timezone.now)
    username = models.CharField(max_length=50, blank=True, null=True)
    statusfield = models.BooleanField(default=False, null=True)
    def __str__(self):
        return self.sheetname
