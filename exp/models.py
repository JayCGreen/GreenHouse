from django.db import models

# Create your models here.

class Tech(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Edu(models.Model):
    name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    major = models.CharField(max_length=100)

class Experience(models.Model):
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    desc = models.TextField()
    techUsed = models.ManyToManyField(Tech, blank=True)
    start = models.DateField(default="1998-12-25")
    end = models.DateField(default="1998-12-25")

    class Meta:
        ordering = ["-start"]
        
    def __str__(self):
        return self.company



    