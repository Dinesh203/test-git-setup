from django.db import models
import datetime

# Create your models here


class Blogs(models.Model):
    title = models.CharField(max_length=100, default="")
    description = models.TextField(default="")

    def __str__(self):
        return self.title



  # image = models.ImageField(upload_to='images', default="")
    # added_date = models.DateTimeField(default="")