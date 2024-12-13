from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import os

# Create your models here.
def get_file_path(request, filename):
    original_filename= filename
    filename = "%s" % (original_filename)
    return os.path.join('uploads/', filename)

class Product(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to = get_file_path, null=True, blank=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    message = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return self.name