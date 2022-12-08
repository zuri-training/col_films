from django.db import models
import uuid

RATINGS = (
    ('5', '5 Star'),
    ('4', '4 Star'),
    ('3', '3 Star'),
    ('2', '2 Star'),
    ('1', '1 Star'),
    
)
# Create your models here.

class User(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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

class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    description = models.TextField()
    created = models.DateField()
    rated = models.CharField(choices=RATINGS, max_length=1)
    duration = models.CharField(max_length=10)
    actors = models.CharField(max_length=400)
    poster = models.ImageField()

    def __str__(self):
        return {self.title: self.description}

