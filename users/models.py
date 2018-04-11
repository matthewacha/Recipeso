# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    email= models.EmailField(max_length=40)
    password=models.CharField(max_length=100)
    date_added=models.DateTimeField(default = timezone.now)

    def __str__(self):
        return 'email: {}'.format(self.email)
    
