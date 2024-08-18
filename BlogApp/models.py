from django.db import models

# Create your models here.


class Post(models.Model):
    id = models.AutoField(primary_key=True) 
    title = models.CharField(max_length=70)
    descrption = models.CharField(max_length=700)
