from django.db import models
from exp.models import Tech

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    shortdesc = models.TextField()
    tech = models.ManyToManyField(Tech, blank=True)
    longdesc = models.TextField()
    gitlink = models.CharField(max_length=100, blank=True, default="")
    demolink = models.CharField(max_length=100, blank=True, default="")
    def __str__(self):
        return self.title
