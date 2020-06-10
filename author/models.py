from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Author(models.Model):
    #author_user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    author_name = models.CharField(unique=True , max_length=20)
    author_age = models.IntegerField()
    author_nationality = models.CharField(max_length=20)
    author_phone_number = models.IntegerField()


    def __str__(self):
        return self.author_name

        
