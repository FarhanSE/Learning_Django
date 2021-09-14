from django.db import models
import uuid
from users.models import Profiles
# Create your models here.

class Project(models.Model):
    owner = models.ForeignKey(Profiles, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, blank=True, null=True)
    demo_link = models.CharField(max_length=1000)
    source_link = models.CharField(max_length=1000, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    feature_image = models.ImageField(blank=True, null=True, default="default.jpg")
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    

    def __str__(self):
        return self.title

class Review(models.Model):
    Vote_Choice = (
        ('up', 'Up vote'),
        ('down', 'down vote')
    )
    # owner =
    project = models.ForeignKey(Project, on_delete=models.CASCADE) 
    body = models.TextField(max_length=500, blank=False, null=False)
    value = models.TextField(max_length=200, choices=Vote_Choice)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.value




class Tag(models.Model):
    name = models.CharField(max_length=400, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.name