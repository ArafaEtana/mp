from django.db import models

# Create your models here.
class postJob(models.Model):
    project_name= models.CharField(max_length=100)
    about_project=models.CharField(max_length=150 )