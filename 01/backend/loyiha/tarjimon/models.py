from django.db import models

# Create your models here.
class Lugat(models.Model):
    
    inglizcha = models.CharField('Inglizcha', max_length=128)
    uzbekcha = models.CharField('Ozbekcha', max_length=128)