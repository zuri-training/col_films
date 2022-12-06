from django.db import models

# Create your models here.

class User(models.Model):
    first_name= models.CharField("Firstname", max_length=100)
    last_name= models.CharField("Lastname", max_length=100)
    username = models.CharField("Username", max_length=50, unique=True, null=True)
    email = models.CharField("Email Address", max_length=250, unique=True)
    password = models.CharField("Password", max_length=50)
    school = models.CharField("School", max_length=50)
    created_at = models.DateField("Registration Date", auto_now_add=True)
    is_staff = models.BooleanField("Staff", default=False)
    is_member = models.BooleanField("Member", default=False)
    verified = models.BooleanField("Verified", default=False)

    def __str__(self):
        return self.first_name

