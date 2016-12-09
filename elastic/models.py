from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField()
    author = models.ForeignKey(User, null=True, blank=True)
    pub_date = models.DateTimeField(auto_now=True)
