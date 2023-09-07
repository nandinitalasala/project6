from django.db import models

# Create your models here.
class LoginData(models.Model):
    email=models.CharField(max_length=60)
    password=models.CharField(max_length=60)

class SignupData(models.Model):
    first_name=models.CharField(max_length=60)
    last_name=models.CharField(max_length=60)
    dob=models.DateField()
    Email=models.EmailField(max_length=60)
    phone=models.BigIntegerField()