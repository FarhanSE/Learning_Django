from django.db import models
from django.contrib.auth.models import User


import uuid
# Create your models here.

class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=300)
    short_intro = models.CharField(max_length=500)
    bio = models.TextField(max_length=2000)
    location = models.CharField(max_length=200)
    profile_image = models.ImageField(null=True, blank=True, default = 'profiles/user-default.png', upload_to = 'profiles/')
    github = models.CharField(max_length=400, blank=True, null=True)
    linkedin = models.CharField(max_length=400, blank=True, null=True)
    youtube = models.CharField(max_length=400, blank=True, null=True)
    website = models.CharField(max_length=400, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return str(self.user)


class Skills(models.Model):
    owner = models.ForeignKey(Profiles, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

