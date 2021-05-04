from django.db import models
from .slice import *


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50, default="", unique=True)
    page_number = models.PositiveIntegerField()
    page = models.ImageField(null=True, blank=True, upload_to="img/%y")

    def __str__(self):
        return self.title

