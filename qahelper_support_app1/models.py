from django.db import models

# Create your models here.
class testItGroupData(models.Model):
    tetItURL = models.CharField(max_length=20, blank=False)
    projectName = models.CharField(max_length=20, blank=False)

