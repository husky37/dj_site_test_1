from django.db import models


# Create your models here.
# Джанго модели это на самом деле таблици в базе данных

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone_number = models.IntegerField(null=True)
    joined_data = models.DateField(null=True)

