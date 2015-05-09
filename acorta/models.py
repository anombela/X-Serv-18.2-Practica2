from django.db import models

# users: anombela password: anombela

# Create your models here.

class Url(models.Model):
    url= models.CharField(max_length=256)
