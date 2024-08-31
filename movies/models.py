from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    emoji = models.CharField(max_length=10)

    def __str__(self):
        return self.title