# models.py->DBのテーブルやカラムを設定する
from django.db import models

# Create your models here.

CHOICE = (('red','high'),
          ('green','normal'),
          ('blue','low',)
          )

class todoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(max_length=2000)

    priority = models.CharField(
        max_length=50,
        choices = CHOICE
    )
    duedate = models.DateField()

    def __str__(self):
        return self.title

