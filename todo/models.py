
from django.db import models

# Create your models here.

class todoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(max_length=2000)

    

    def __str__(self):
        return self.title

