from audioop import maxpp
from statistics import mode
from django.db import models

# Create your models here.
# python manage.py makemigrations <- SQL generate
# python manage.py migrate <- execute
# id -> default -> auto inc, uni, pk

class Student(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)